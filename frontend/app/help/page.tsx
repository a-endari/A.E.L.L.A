"use client";

import { motion } from "framer-motion";
import { ArrowLeft, BookOpen, Folder, FileText, Music } from "lucide-react";
import Link from "next/link";

export default function HelpPage() {
    return (
        <main className="min-h-screen bg-slate-950 text-white p-6 md:p-12 relative overflow-hidden">
            {/* Background Gradients */}
            <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
                <div className="absolute top-[-20%] right-[-10%] w-[500px] h-[500px] bg-purple-600/10 rounded-full blur-[120px]" />
                <div className="absolute bottom-[-20%] left-[-10%] w-[500px] h-[500px] bg-blue-600/10 rounded-full blur-[120px]" />
            </div>

            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="max-w-3xl mx-auto space-y-12"
            >
                <Link href="/" className="inline-flex items-center gap-2 text-slate-400 hover:text-white transition-colors">
                    <ArrowLeft size={20} />
                    Back to App
                </Link>

                <div className="space-y-4">
                    <h1 className="text-4xl md:text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-blue-400">
                        Obsidian Export Guide
                    </h1>
                    <p className="text-lg text-slate-400">
                        How to import your vocabulary list into your Obsidian Vault with full audio support.
                    </p>
                </div>

                <div className="space-y-8">
                    {/* Step 1 */}
                    <section className="space-y-4 p-6 bg-white/5 border border-white/10 rounded-2xl">
                        <h2 className="text-2xl font-bold flex items-center gap-3">
                            <span className="flex items-center justify-center w-8 h-8 rounded-full bg-purple-500/20 text-purple-300 text-sm">1</span>
                            Download & Extract
                        </h2>
                        <p className="text-slate-300">
                            When you click "Export Obsidian Note", you will download a <code>.zip</code> file.
                            Extract this file. You will see:
                        </p>
                        <ul className="grid gap-3 sm:grid-cols-2">
                            <li className="flex items-center gap-3 p-3 bg-slate-900/50 rounded-lg">
                                <FileText className="text-blue-400" size={20} />
                                <span className="text-sm">Words.md (Your Notes)</span>
                            </li>
                            <li className="flex items-center gap-3 p-3 bg-slate-900/50 rounded-lg">
                                <Folder className="text-yellow-400" size={20} />
                                <span className="text-sm">Media/ (Audio Files)</span>
                            </li>
                        </ul>
                    </section>

                    {/* Step 2 */}
                    <section className="space-y-4 p-6 bg-white/5 border border-white/10 rounded-2xl">
                        <h2 className="text-2xl font-bold flex items-center gap-3">
                            <span className="flex items-center justify-center w-8 h-8 rounded-full bg-purple-500/20 text-purple-300 text-sm">2</span>
                            Import to Obsidian
                        </h2>
                        <p className="text-slate-300">
                            Drag the <strong>Words.md</strong> file and the <strong>Media</strong> folder directly into your Obsidian Vault.
                        </p>
                        <div className="p-4 bg-slate-900/50 rounded-xl border border-white/5 text-sm text-slate-400">
                            <p className="font-semibold text-purple-300 mb-2">💡 Tip: Attachment Settings</p>
                            <p>
                                Ensure Obsidian can find the new audio files. Go to
                                <span className="text-white mx-1">Settings &gt; Files & Links</span>.
                            </p>
                            <p className="mt-2">
                                If 'Default location for new attachments' is set to 'Same folder as current file' or 'In subfolder under current folder',
                                keeping the <code>Media</code> folder next to <code>Words.md</code> works perfectly.
                            </p>
                        </div>
                    </section>

                    {/* Step 3 */}
                    <section className="space-y-4 p-6 bg-white/5 border border-white/10 rounded-2xl">
                        <h2 className="text-2xl font-bold flex items-center gap-3">
                            <span className="flex items-center justify-center w-8 h-8 rounded-full bg-purple-500/20 text-purple-300 text-sm">3</span>
                            Review your Notes
                        </h2>
                        <p className="text-slate-300">
                            Open <code>Words.md</code> in Obsidian. You should see your words, synonyms in callouts, and playable audio players.
                        </p>
                        <div className="flex items-center gap-4 p-4 bg-purple-500/10 border border-purple-500/20 rounded-lg">
                            <Music className="text-purple-400" />
                            <span className="text-purple-200 text-sm">Audio players will look like: <code>![[Haus.mp3]]</code></span>
                        </div>
                    </section>
                </div>

            </motion.div>
        </main>
    );
}
