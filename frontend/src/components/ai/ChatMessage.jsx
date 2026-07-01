import { motion } from "framer-motion";
import { Bot, User } from "lucide-react";
import ReactMarkdown from "react-markdown";
import SourceCard from "./SourceCard.jsx";

export default function ChatMessage({
  role,
  content,
  sources = [],
  intent,
}) {
  const isUser = role === "user";

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.25 }}
      className={`flex gap-5 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      {/* Assistant Avatar */}
      {!isUser && (
        <div className="w-12 h-12 rounded-2xl bg-white/5 border border-border flex items-center justify-center shrink-0">
          <Bot size={22} className="text-primary-lighter" />
        </div>
      )}

      {/* Message Area */}
      <div
        className={`flex flex-col ${
          isUser ? "items-end" : "items-start"
        } flex-1`}
      >
        {/* Bubble */}
        <div
          className={`${
            isUser
              ? "bg-primary text-white max-w-5xl rounded-3xl rounded-br-lg"
              : "bg-card border border-border rounded-3xl rounded-bl-lg w-full"
          } px-8 py-6 shadow-card`}
        >
          {isUser ? (
            <p className="whitespace-pre-wrap text-[19px] leading-9">
              {content}
            </p>
          ) : (
            <div className="markdown-body text-[18px] leading-9">
              <ReactMarkdown>{content}</ReactMarkdown>
            </div>
          )}
        </div>

        {/* Intent */}
        {!isUser && intent && (
          <div className="mt-3 text-sm text-subtle">
            Intent :
            <span className="ml-2 text-primary-lighter font-semibold">
              {intent}
            </span>
          </div>
        )}

        {/* Sources */}
        {!isUser && sources.length > 0 && (
          <div className="flex flex-wrap gap-4 mt-5 w-full">
            {sources.map((source, index) => (
              <SourceCard
                key={index}
                document={source.document}
                page={source.page}
                category={source.category}
              />
            ))}
          </div>
        )}
      </div>

      {/* User Avatar */}
      {isUser && (
        <div className="w-12 h-12 rounded-2xl bg-primary flex items-center justify-center shrink-0">
          <User size={22} className="text-white" />
        </div>
      )}
    </motion.div>
  );
}