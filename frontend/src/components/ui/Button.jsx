const variants = {
  primary: 'bg-primary hover:bg-primary-dark text-white shadow-glow',
  ghost: 'bg-transparent hover:bg-white/5 text-muted hover:text-slate-100 border border-border',
  danger: 'bg-danger/15 hover:bg-danger/25 text-danger border border-danger/30',
}

export default function Button({ children, variant = 'primary', className = '', icon: Icon, ...props }) {
  return (
    <button
      className={`inline-flex items-center justify-center gap-2 rounded-xl px-5 py-2.5 text-sm font-medium transition-colors duration-150 disabled:opacity-50 disabled:cursor-not-allowed ${variants[variant]} ${className}`}
      {...props}
    >
      {Icon && <Icon size={17} />}
      {children}
    </button>
  )
}
