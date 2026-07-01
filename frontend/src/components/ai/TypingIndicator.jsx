import { motion } from 'framer-motion'
import { Bot } from 'lucide-react'

export default function TypingIndicator() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      className="flex gap-4"
    >
      <div className="w-9 h-9 rounded-xl flex items-center justify-center shrink-0 mt-0.5 bg-white/5 border border-border">
        <Bot size={16} className="text-primary-lighter" />
      </div>
      <div className="bg-card border border-border rounded-2xl rounded-tl-md px-5 py-3.5 flex items-center gap-3 shadow-card">
        <div className="flex items-center gap-1.5">
          <span className="w-2 h-2 rounded-full bg-primary-light animate-bounce [animation-delay:-0.3s]" />
          <span className="w-2 h-2 rounded-full bg-primary-light animate-bounce [animation-delay:-0.15s]" />
          <span className="w-2 h-2 rounded-full bg-primary-light animate-bounce" />
        </div>
        <span className="text-sm text-subtle">Thinking through the knowledge base…</span>
      </div>
    </motion.div>
  )
}
