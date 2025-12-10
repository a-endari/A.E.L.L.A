import type { Metadata } from "next";
import { Outfit } from "next/font/google";
import "./globals.css";

const outfit = Outfit({
  subsets: ["latin"],
  variable: "--font-outfit",
});

export const metadata: Metadata = {
  title: "Universal Language App",
  description: "Learn languages with ease. Universal. Simple. Powerful.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${outfit.variable} antialiased min-h-screen bg-slate-950 text-slate-100 selection:bg-purple-500/30`}
      >
        {children}
      </body>
    </html>
  );
}
