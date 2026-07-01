import { useEffect, useRef, useState } from 'react'
import { useMutation } from '@tanstack/react-query'
import { motion } from 'framer-motion'
import { Trash2, Sparkles, AlertTriangle } from 'lucide-react'
import ChatMessage from '../components/ai/ChatMessage.jsx'
import ChatInput from '../components/ai/ChatInput.jsx'
import TypingIndicator from '../components/ai/TypingIndicator.jsx'
import { sendChatMessage } from '../services/api.js'

const WELCOME = {
  role: 'assistant',
  content:
    "Hello, I'm your **Clinical Knowledge Assistant**. Ask me about treatment guidelines, drug protocols, or hospital operations, and I'll answer using the connected knowledge base, with sources cited.",
  sources: [],
}

const SUGGESTIONS = [
  'What is the treatment protocol for dengue?',
  'What are the warning signs of sepsis?',
  'Summarize the discharge criteria for ICU patients',
  'What is tuberculosis?',
]

export default function Assistant() {
  const [messages, setMessages] = useState([WELCOME])
  const scrollRef = useRef(null)

  const { mutate, isPending } = useMutation({
    mutationFn: sendChatMessage,
    onSuccess: (data) => {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: data?.answer || 'No answer was returned by the assistant.',
          sources: data?.sources || [],
          intent: data?.intent,
        },
      ])
    },
    onError: () => {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content:
            "I couldn't reach the clinical knowledge backend. Please confirm the API at `http://127.0.0.1:8000` is running and try again.",
          sources: [],
          error: true,
        },
      ])
    },
  })

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: 'smooth' })
  }, [messages, isPending])

  function handleSend(question) {
    setMessages((prev) => [...prev, { role: 'user', content: question }])
    mutate(question)
  }

  function handleClear() {
    setMessages([WELCOME])
  }

  return (
    <div className="flex flex-col h-[calc(100vh-5rem)] w-full">
      <div className="flex items-center justify-between px-6 md:px-8 py-4 border-b border-border bg-card/30">
        <div className="flex items-center gap-2.5 text-sm text-subtle">
          <Sparkles size={16} className="text-primary-light" />
          <span>
            Retrieval-Augmented Generation &middot; connected to{' '}
            <code className="text-slate-300 bg-cardsoft border border-border rounded px-1.5 py-0.5 text-[13px]">/ai/chat</code>
          </span>
        </div>
        <button
          onClick={handleClear}
          className="flex items-center gap-2 text-sm text-subtle hover:text-danger transition-colors px-3 py-2 rounded-lg hover:bg-danger/10"
        >
          <Trash2 size={15} />
          Clear Chat
        </button>
      </div>

      <div ref={scrollRef} className="flex-1 overflow-y-auto">
        <div className="w-full px-16 xl:px-24 py-10 space-y-10">
          {messages.map((m, i) => (
            <ChatMessage key={i} role={m.role} content={m.content} sources={m.sources} intent={m.intent} />
          ))}
          {isPending && <TypingIndicator />}

          {messages.length === 1 && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.15 }}
              className="flex flex-wrap gap-4 pl-16"
            >
              {SUGGESTIONS.map((s) => (
                <button
                  key={s}
                  onClick={() => handleSend(s)}
                  className="text-base text-left bg-card border border-border hover:border-primary/40 hover:bg-cardhover rounded-full px-6 py-4 text-muted hover:text-slate-100 transition-colors"
                >
                  {s}
                </button>
              ))}
            </motion.div>
          )}
        </div>
      </div>

      <div className="w-full px-16 xl:px-24">
        <ChatInput onSend={handleSend} disabled={isPending} />
        <p className="flex items-center justify-center gap-1.5 text-xs text-subtle px-4 pb-4">
          <AlertTriangle size={12} />
          AI responses are generated from the connected knowledge base and should be verified by a qualified clinician.
        </p>
      </div>
    </div>
  )
}
