import { useEffect, useRef, useState } from "react";
import { Send, Sparkles } from "lucide-react";

const MAX_HEIGHT = 260;

export default function ChatInput({ onSend, disabled }) {
  const [value, setValue] = useState("");
  const textareaRef = useRef(null);

  useEffect(() => {
    const el = textareaRef.current;
    if (!el) return;

    el.style.height = "auto";
    el.style.height = `${Math.min(el.scrollHeight, MAX_HEIGHT)}px`;
  }, [value]);

  function handleSubmit(e) {
    e.preventDefault();

    const message = value.trim();

    if (!message || disabled) return;

    onSend(message);

    setValue("");
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="pb-6 pt-4">
      <div className="relative flex items-end gap-5 rounded-[32px] border border-border bg-card px-6 py-5 shadow-xl focus-within:border-primary/60">

        <div className="w-12 h-12 rounded-2xl bg-primary/15 flex items-center justify-center shrink-0">
          <Sparkles size={22} className="text-primary-lighter" />
        </div>

        <textarea
          ref={textareaRef}
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          rows={1}
          disabled={disabled}
          placeholder="Ask anything about clinical guidelines, hospital operations, patients, ICU beds, billing..."
          className="flex-1 resize-none bg-transparent outline-none text-[19px] leading-9 text-slate-100 placeholder:text-slate-500 min-h-[80px] max-h-[260px]"
        />

        <button
          type="submit"
          disabled={disabled || !value.trim()}
          className="w-14 h-14 rounded-2xl bg-primary hover:bg-blue-700 disabled:opacity-40 flex items-center justify-center transition-all"
        >
          <Send size={24} className="text-white" />
        </button>

      </div>

      <p className="text-center text-sm text-subtle mt-4">
        Press <b>Enter</b> to send • <b>Shift + Enter</b> for a new line
      </p>
    </form>
  );
}