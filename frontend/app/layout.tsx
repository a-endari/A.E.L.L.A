import type { Metadata } from "next";
import { Outfit } from "next/font/google";
import "./globals.css";

const outfit = Outfit({
  subsets: ["latin"],
  variable: "--font-outfit",
});

export const metadata: Metadata = {
  title: "AELLA - Universal Language App",
  description: "Your AI-Enhanced Language Learning Assistant. Create flashcards, export to Anki & Obsidian.",
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
