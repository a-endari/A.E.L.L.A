"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Search, Volume2, Sparkles, Download, ArrowRight, BookOpen } from "lucide-react";
import axios from "axios";
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// Types for API Reference
interface WordData {
  original_word: string;
  clean_word: string;
  definition: string;
  audio_url: string | null;
}

export default function Home() {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState<WordData | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setError(null);
    setData(null);

    try {
      const response = await axios.post("http://localhost:8000/api/lookup", {
        word: query,
      });
      setData(response.data);
    } catch (err) {
      setError("Could not find word. Please try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const playAudio = () => {
    if (data?.audio_url) {
      const audio = new Audio(data.audio_url);
      audio.play();
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-6 relative overflow-hidden">
      {/* Background Gradients */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div className="absolute top-[-20%] left-[-10%] w-[500px] h-[500px] bg-purple-600/20 rounded-full blur-[120px]" />
        <div className="absolute bottom-[-20%] right-[-10%] w-[500px] h-[500px] bg-blue-600/20 rounded-full blur-[120px]" />
      </div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-3xl space-y-12"
      >
        {/* Header */}
        <div className="text-center space-y-4">
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-sm text-purple-300 mb-4"
          >
            <Sparkles size={14} />
            <span>Universal Language Assistant</span>
          </motion.div>

          <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-200 to-slate-400">
            Learn German <br />
            <span className="text-purple-400">Instantly.</span>
          </h1>

          <p className="text-lg text-slate-400 max-w-lg mx-auto leading-relaxed">
            Enter a word to get instant translations, pronunciations, and flashcards. Note: Backend must be running on port 8000.
          </p>
        </div>

        {/* Search Input */}
        <form onSubmit={handleSearch} className="relative max-w-xl mx-auto w-full group">
          <div className="absolute inset-y-0 left-4 flex items-center pointer-events-none text-slate-500 group-focus-within:text-purple-400 transition-colors">
            <Search size={20} />
          </div>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Type a German word (e.g. 'Haus')..."
            className="w-full bg-white/5 border border-white/10 rounded-2xl py-5 pl-12 pr-6 text-xl text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500/50 transition-all shadow-xl shadow-black/20"
          />
          <button
            type="submit"
            disabled={loading || !query}
            className="absolute inset-y-2 right-2 px-4 bg-white/10 hover:bg-white/20 text-white rounded-xl transition-all disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? (
              <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
            ) : (
              <ArrowRight size={20} />
            )}
          </button>
        </form>

        {/* Results Card */}
        <AnimatePresence mode="wait">
          {error && (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              className="p-4 rounded-xl bg-red-500/10 border border-red-500/20 text-red-300 text-center"
            >
              {error}
            </motion.div>
          )}

          {data && (
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              className="bg-white/5 border border-white/10 rounded-3xl p-8 backdrop-blur-xl shadow-2xl relative overflow-hidden"
            >
              {/* Card Decoration */}
              <div className="absolute top-0 right-0 p-32 bg-purple-500/5 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none" />

              <div className="relative z-10 flex flex-col md:flex-row gap-8">
                {/* Left: Word & Audio */}
                <div className="flex-1 space-y-6">
                  <div className="space-y-2">
                    <p className="text-sm font-medium text-purple-300 uppercase tracking-wider">German</p>
                    <div className="flex items-center gap-4">
                      <h2 className="text-5xl font-bold text-white">{data.original_word}</h2>
                      {data.audio_url && (
                        <button
                          onClick={playAudio}
                          className="p-3 bg-purple-500/20 hover:bg-purple-500/40 text-purple-300 rounded-full transition-all hover:scale-105 active:scale-95"
                          title="Play Pronunciation"
                        >
                          <Volume2 size={24} />
                        </button>
                      )}
                    </div>
                    {data.original_word !== data.clean_word && (
                      <p className="text-slate-500">Root: {data.clean_word}</p>
                    )}
                  </div>

                  <div className="flex gap-3">
                    <button className="flex items-center gap-2 px-4 py-2 bg-slate-800 hover:bg-slate-700/80 rounded-lg text-sm text-slate-300 transition-colors border border-white/5">
                      <BookOpen size={16} />
                      Save to Collection
                    </button>
                    <button className="flex items-center gap-2 px-4 py-2 bg-slate-800 hover:bg-slate-700/80 rounded-lg text-sm text-slate-300 transition-colors border border-white/5">
                      <Download size={16} />
                      Download Anki Card
                    </button>
                  </div>
                </div>

                {/* Vertical Divider */}
                <div className="hidden md:block w-px bg-white/10" />

                {/* Right: Definition */}
                <div className="flex-1 space-y-4">
                  <p className="text-sm font-medium text-blue-300 uppercase tracking-wider">Persian Definition</p>
                  <div className="prose prose-invert prose-p:text-slate-300 prose-headings:text-white max-h-[300px] overflow-y-auto pr-2 custom-scrollbar">
                    {/* Render HTML content safely */}
                    <div dangerouslySetInnerHTML={{ __html: data.definition.replace(/\n/g, '<br/>') }} />
                  </div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

      </motion.div>
    </main>
  );
}
