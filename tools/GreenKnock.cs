using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;

public static class GreenKnock {
  static bool IsKey(Color c) {
    if (c.A < 8) return true;
    int max = Math.Max(c.R, Math.Max(c.G, c.B));
    int min = Math.Min(c.R, Math.Min(c.G, c.B));
    if (c.G > 90 && c.G >= c.R + 35 && c.G >= c.B + 25) return true;
    if (c.G > 140 && c.G > c.R && c.G > c.B && (c.G - min) > 40) return true;
    if (c.G > 180 && c.R < 160 && c.B < 160) return true;
    return false;
  }

  public static void Run(string srcPath, string dstPath) {
    using (Bitmap src = new Bitmap(srcPath)) {
      int w = src.Width;
      int h = src.Height;
      Bitmap bmp = new Bitmap(w, h, PixelFormat.Format32bppArgb);
      using (Graphics g = Graphics.FromImage(bmp)) {
        g.DrawImage(src, 0, 0, w, h);
      }
      Queue<Point> q = new Queue<Point>();
      int[] dx = new int[] { 1, -1, 0, 0 };
      int[] dy = new int[] { 0, 0, 1, -1 };
      bool[] seen = new bool[w * h];
      for (int x = 0; x < w; x++) {
        Try(bmp, q, seen, x, 0, w, h);
        Try(bmp, q, seen, x, h - 1, w, h);
      }
      for (int y = 0; y < h; y++) {
        Try(bmp, q, seen, 0, y, w, h);
        Try(bmp, q, seen, w - 1, y, w, h);
      }
      while (q.Count > 0) {
        Point p = q.Dequeue();
        for (int i = 0; i < 4; i++) Try(bmp, q, seen, p.X + dx[i], p.Y + dy[i], w, h);
      }
      for (int y = 1; y < h - 1; y++) {
        for (int x = 1; x < w - 1; x++) {
          Color c = bmp.GetPixel(x, y);
          if (c.A < 8) continue;
          if (!IsKey(c)) continue;
          int n = 0;
          for (int i = 0; i < 4; i++) {
            Color nb = bmp.GetPixel(x + dx[i], y + dy[i]);
            if (nb.A < 8) n++;
          }
          if (n >= 2) bmp.SetPixel(x, y, Color.FromArgb(0, 0, 0, 0));
        }
      }
      bmp.Save(dstPath, ImageFormat.Png);
      bmp.Dispose();
    }
  }

  static void Try(Bitmap bmp, Queue<Point> q, bool[] seen, int x, int y, int w, int h) {
    if (x < 0 || y < 0 || x >= w || y >= h) return;
    int i = y * w + x;
    if (seen[i]) return;
    Color c = bmp.GetPixel(x, y);
    if (!IsKey(c)) return;
    seen[i] = true;
    bmp.SetPixel(x, y, Color.FromArgb(0, 0, 0, 0));
    q.Enqueue(new Point(x, y));
  }
}
