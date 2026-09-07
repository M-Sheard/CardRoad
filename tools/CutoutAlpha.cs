using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.Drawing.Text;

public static class CutoutAlpha16 {
  static readonly Color Paper = Color.FromArgb(255, 168, 156, 122);
  static readonly Color KraftNear = Color.FromArgb(255, 132, 98, 58);
  static readonly Color KraftFar = Color.FromArgb(255, 74, 52, 32);
  static readonly Color PlateFace = Color.FromArgb(255, 196, 158, 108);
  static readonly Color PlateShade = Color.FromArgb(255, 158, 118, 74);
  static readonly Color Letter = Color.FromArgb(255, 42, 26, 12);

  static bool IsOldHalo(Color c) {
    if (c.A < 8) return true;
    if (Math.Abs(c.R - 168) < 14 && Math.Abs(c.G - 156) < 14 && Math.Abs(c.B - 122) < 14) return true;
    if (Math.Abs(c.R - 186) < 14 && Math.Abs(c.G - 168) < 14 && Math.Abs(c.B - 128) < 14) return true;
    int chroma = Math.Max(c.R, Math.Max(c.G, c.B)) - Math.Min(c.R, Math.Min(c.G, c.B));
    int lum = (c.R + c.G + c.B) / 3;
    if (lum >= 200 && chroma < 22) return true;
    if (lum >= 175 && chroma < 40 && c.B + 18 >= c.R) return true;
    return false;
  }

  static bool IsKraft(Color c) {
    if (c.A < 8) return false;
    if (Math.Abs(c.R - KraftFar.R) < 8 && Math.Abs(c.G - KraftFar.G) < 8 && Math.Abs(c.B - KraftFar.B) < 8) return true;
    if (Math.Abs(c.R - KraftNear.R) < 8 && Math.Abs(c.G - KraftNear.G) < 8 && Math.Abs(c.B - KraftNear.B) < 8) return true;
    if (Math.Abs(c.R - 78) < 8 && Math.Abs(c.G - 56) < 8 && Math.Abs(c.B - 34) < 8) return true;
    if (Math.Abs(c.R - 118) < 10 && Math.Abs(c.G - 88) < 10 && Math.Abs(c.B - 52) < 10) return true;
    return false;
  }

  static bool IsCorePaint(Color c) {
    if (c.A < 8) return false;
    if (IsOldHalo(c) || IsKraft(c)) return false;
    int chroma = Math.Max(c.R, Math.Max(c.G, c.B)) - Math.Min(c.R, Math.Min(c.G, c.B));
    int lum = (c.R + c.G + c.B) / 3;
    if (chroma >= 18) return true;
    if (lum < 175) return true;
    return false;
  }

  static bool[] LargestCore(Bitmap bmp, int w, int h) {
    int n = w * h;
    bool[] core = new bool[n];
    for (int y = 0; y < h; y++) {
      for (int x = 0; x < w; x++) {
        if (IsCorePaint(bmp.GetPixel(x, y))) core[y * w + x] = true;
      }
    }
    int[] dx4 = new int[] { 1, -1, 0, 0 };
    int[] dy4 = new int[] { 0, 0, 1, -1 };
    int[] label = new int[n];
    int bestCount = 0;
    int bestLabel = 0;
    int nextLabel = 1;
    Queue<int> q = new Queue<int>();
    for (int i = 0; i < n; i++) {
      if (!core[i] || label[i] != 0) continue;
      int lab = nextLabel++;
      int count = 0;
      q.Enqueue(i);
      label[i] = lab;
      while (q.Count > 0) {
        int p = q.Dequeue();
        count++;
        int x = p % w;
        int y = p / w;
        for (int k = 0; k < 4; k++) {
          int xx = x + dx4[k];
          int yy = y + dy4[k];
          if (xx < 0 || yy < 0 || xx >= w || yy >= h) continue;
          int j = yy * w + xx;
          if (!core[j] || label[j] != 0) continue;
          label[j] = lab;
          q.Enqueue(j);
        }
      }
      if (count > bestCount) {
        bestCount = count;
        bestLabel = lab;
      }
    }
    for (int i = 0; i < n; i++) {
      if (label[i] == bestLabel) continue;
      bmp.SetPixel(i % w, i / w, Color.FromArgb(0, 0, 0, 0));
      core[i] = false;
    }
    return core;
  }

  static int BootBottom(bool[] core, Bitmap bmp, int w, int h) {
    int yCut = 0;
    for (int y = 1180; y < h; y++) {
      int dark = 0;
      int tan = 0;
      int n = 0;
      for (int x = 0; x < w; x++) {
        if (!core[y * w + x]) continue;
        n++;
        Color c = bmp.GetPixel(x, y);
        int lum = (c.R + c.G + c.B) / 3;
        if (Math.Abs(c.R - 196) < 20 && Math.Abs(c.G - 158) < 20) tan++;
        else if (lum < 115 && c.R > c.B + 12) dark++;
      }
      if (tan > 80 && tan > dark) {
        if (yCut < 1280) yCut = y - 2;
        break;
      }
      if (dark > 40 && dark >= tan) yCut = y;
    }
    if (yCut < 1280) yCut = 1348;
    return yCut + 2;
  }

  static void ReplaceNameplate(Bitmap bmp, bool[] core, int w, int h) {
    int cutY = BootBottom(core, bmp, w, h);
    int minX = w, maxX = 0;
    for (int y = 1180; y < cutY; y++) {
      for (int x = 0; x < w; x++) {
        if (!core[y * w + x]) continue;
        if (x < minX) minX = x;
        if (x > maxX) maxX = x;
      }
    }
    for (int y = cutY; y < h; y++) {
      for (int x = 0; x < w; x++) {
        bmp.SetPixel(x, y, Color.FromArgb(0, 0, 0, 0));
        core[y * w + x] = false;
      }
    }

    int plateW = 480;
    int plateH = 124;
    int px = (minX + maxX) / 2 - plateW / 2;
    int py = cutY - 8;
    if (px < 12) px = 12;
    if (px + plateW > w - 28) px = w - 28 - plateW;
    if (py + plateH > h - 28) py = h - 28 - plateH;

    using (Graphics g = Graphics.FromImage(bmp)) {
      g.SmoothingMode = SmoothingMode.AntiAlias;
      g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
      using (GraphicsPath path = Rounded(px, py, plateW, plateH, 14)) {
        g.FillPath(new SolidBrush(PlateFace), path);
      }
      StringFormat fmt = new StringFormat();
      fmt.Alignment = StringAlignment.Center;
      fmt.LineAlignment = StringAlignment.Center;
      RectangleF textBox = new RectangleF(px + 12, py + 6, plateW - 24, plateH - 22);
      using (Font font = new Font(FontFamily.GenericSerif, 64, FontStyle.Bold, GraphicsUnit.Pixel)) {
        SizeF sz = g.MeasureString("TOMAS", font);
        float tx = px + (plateW - sz.Width) / 2f;
        float ty = py + 36;
        g.DrawString("TOMAS", font, new SolidBrush(Letter), tx, ty);
        g.Flush();
      }
    }
  }

  static GraphicsPath Rounded(int x, int y, int w, int h, int r) {
    GraphicsPath p = new GraphicsPath();
    int d = r * 2;
    p.AddArc(x, y, d, d, 180, 90);
    p.AddArc(x + w - d, y, d, d, 270, 90);
    p.AddArc(x + w - d, y + h - d, d, d, 0, 90);
    p.AddArc(x, y + h - d, d, d, 90, 90);
    p.CloseFigure();
    return p;
  }

  static void AddCardboardSlab(Bitmap bmp, bool[] core, int w, int h) {
    int ox = 16;
    int oy = 22;
    for (int y = 0; y < h; y++) {
      for (int x = 0; x < w; x++) {
        if (!core[y * w + x]) continue;
        for (int t = 1; t <= oy; t++) {
          int xx = x + ox * t / oy;
          int yy = y + t;
          if (xx < 0 || yy < 0 || xx >= w || yy >= h) continue;
          if (core[yy * w + xx]) continue;
          Color cur = bmp.GetPixel(xx, yy);
          if (cur.A >= 8 && !IsOldHalo(cur) && !IsKraft(cur)) continue;
          bmp.SetPixel(xx, yy, t < oy / 2 ? KraftNear : KraftFar);
        }
      }
    }
  }

  static void AddHalo(Bitmap bmp, bool[] core, int w, int h, int passes) {
    int n = w * h;
    int[] dx8 = new int[] { 1, -1, 0, 0, 1, 1, -1, -1 };
    int[] dy8 = new int[] { 0, 0, 1, -1, 1, -1, 1, -1 };
    bool[] halo = new bool[n];
    bool[] seed = (bool[])core.Clone();
    for (int pass = 0; pass < passes; pass++) {
      Array.Clear(halo, 0, halo.Length);
      for (int y = 1; y < h - 1; y++) {
        for (int x = 1; x < w - 1; x++) {
          int i = y * w + x;
          if (seed[i]) continue;
          bool nextTo = false;
          for (int k = 0; k < 8; k++) {
            if (seed[(y + dy8[k]) * w + (x + dx8[k])]) { nextTo = true; break; }
          }
          if (nextTo) halo[i] = true;
        }
      }
      for (int i = 0; i < halo.Length; i++) {
        if (!halo[i]) continue;
        seed[i] = true;
        int x = i % w;
        int y = i / w;
        Color existing = bmp.GetPixel(x, y);
        if (existing.A >= 8 && !IsOldHalo(existing) && !IsKraft(existing) && !core[i]) continue;
        if (existing.A >= 8 && !IsOldHalo(existing) && !IsKraft(existing)) continue;
        bmp.SetPixel(x, y, Paper);
      }
    }
  }

  public static void Run(string srcPath, string dstPath) {
    using (Bitmap src = new Bitmap(srcPath)) {
      int w = src.Width;
      int h = src.Height;
      Bitmap bmp = new Bitmap(w, h, PixelFormat.Format32bppArgb);
      using (Graphics g = Graphics.FromImage(bmp)) {
        g.DrawImage(src, 0, 0, w, h);
      }

      bool[] core = LargestCore(bmp, w, h);
      ReplaceNameplate(bmp, core, w, h);
      int n = w * h;
      core = new bool[n];
      for (int y = 0; y < h; y++) {
        for (int x = 0; x < w; x++) {
          if (IsCorePaint(bmp.GetPixel(x, y))) core[y * w + x] = true;
        }
      }
      AddHalo(bmp, core, w, h, 13);
      Bitmap face = new Bitmap(bmp);
      AddCardboardSlab(bmp, core, w, h);
      for (int y = 0; y < h; y++) {
        for (int x = 0; x < w; x++) {
          Color f = face.GetPixel(x, y);
          if (f.A >= 8) bmp.SetPixel(x, y, f);
        }
      }
      face.Dispose();

      bmp.Save(dstPath, ImageFormat.Png);
      bmp.Dispose();
    }
  }
}
