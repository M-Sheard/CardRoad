using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;

public static class MatchTomasBevel {
  static readonly Color Oak = Color.FromArgb(255, 214, 148, 78);
  static readonly Color OakHi = Color.FromArgb(255, 242, 196, 128);
  static readonly Color OakDark = Color.FromArgb(255, 72, 42, 14);

  static bool IsWoodRim(Color c) {
    if (c.A < 8) return false;
    int max = Math.Max(c.R, Math.Max(c.G, c.B));
    int min = Math.Min(c.R, Math.Min(c.G, c.B));
    int chroma = max - min;
    int lum = (c.R + c.G + c.B) / 3;
    if (c.R < c.B + 18) return false;
    if (chroma < 18 || chroma > 120) return false;
    if (lum < 70 || lum > 230) return false;
    if (c.G > c.R - 8 && c.B < 80 && chroma > 70) return false;
    return true;
  }

  static bool IsPaint(Color c) {
    if (c.A < 8) return false;
    if (IsWoodRim(c)) return false;
    int chroma = Math.Max(c.R, Math.Max(c.G, c.B)) - Math.Min(c.R, Math.Min(c.G, c.B));
    int lum = (c.R + c.G + c.B) / 3;
    if (chroma >= 16) return true;
    if (lum < 165) return true;
    return false;
  }

  public static void Run(string srcPath, string dstPath) {
    using (Bitmap src = new Bitmap(srcPath)) {
      int w = src.Width;
      int h = src.Height;
      Bitmap bmp = new Bitmap(w, h, PixelFormat.Format32bppArgb);
      using (Graphics g = Graphics.FromImage(bmp)) g.DrawImage(src, 0, 0, w, h);

      int plateY = (int)(h * 0.78);
      int n = w * h;
      bool[] keep = new bool[n];
      for (int y = 0; y < h; y++) {
        for (int x = 0; x < w; x++) {
          Color c = bmp.GetPixel(x, y);
          int i = y * w + x;
          if (y >= plateY && c.A >= 8) keep[i] = true;
          else if (IsPaint(c)) keep[i] = true;
          else bmp.SetPixel(x, y, Color.FromArgb(0, 0, 0, 0));
        }
      }

      Bitmap face = new Bitmap(bmp);
      int[] dx8 = new int[] { 1, -1, 0, 0, 1, 1, -1, -1 };
      int[] dy8 = new int[] { 0, 0, 1, -1, 1, -1, 1, -1 };
      bool[] seed = (bool[])keep.Clone();
      bool[] ring = new bool[n];
      for (int pass = 0; pass < 11; pass++) {
        Array.Clear(ring, 0, n);
        for (int y = 1; y < h - 1; y++) {
          for (int x = 1; x < w - 1; x++) {
            int i = y * w + x;
            if (seed[i]) continue;
            bool next = false;
            for (int k = 0; k < 8; k++) {
              if (seed[(y + dy8[k]) * w + (x + dx8[k])]) { next = true; break; }
            }
            if (next) ring[i] = true;
          }
        }
        for (int i = 0; i < n; i++) {
          if (!ring[i]) continue;
          seed[i] = true;
          int x = i % w;
          int y = i / w;
          Color oak = (x + y) % 5 == 0 ? OakHi : Oak;
          bmp.SetPixel(x, y, oak);
        }
      }

      int ox = 14, oy = 18;
      for (int y = 0; y < h; y++) {
        for (int x = 0; x < w; x++) {
          if (!seed[y * w + x]) continue;
          for (int t = 1; t <= oy; t++) {
            int xx = x + ox * t / oy;
            int yy = y + t;
            if (xx < 0 || yy < 0 || xx >= w || yy >= h) continue;
            if (seed[yy * w + xx]) continue;
            Color cur = bmp.GetPixel(xx, yy);
            if (cur.A >= 8 && !IsWoodRim(cur)) continue;
            bmp.SetPixel(xx, yy, OakDark);
          }
        }
      }

      Bitmap overlay = new Bitmap(face);
      for (int y = 0; y < h; y++) {
        for (int x = 0; x < w; x++) {
          if (!keep[y * w + x]) continue;
          Color f = overlay.GetPixel(x, y);
          if (f.A >= 8) bmp.SetPixel(x, y, f);
        }
      }
      overlay.Dispose();
      face.Dispose();

      bmp.Save(dstPath, ImageFormat.Png);
      bmp.Dispose();
    }
  }
}
