export function Card({ children, className = '', hover = false, ...props }) {
  return (
    <div
      className={`bg-card border border-border rounded-2xl shadow-card ${
        hover ? 'transition-colors duration-150 hover:bg-cardhover hover:border-primary/30' : ''
      } ${className}`}
      {...props}
    >
      {children}
    </div>
  )
}

export function CardHeader({ title, subtitle, action }) {
  return (
    <div className="flex items-center justify-between px-6 pt-6 pb-3">
      <div>
        <h3 className="text-lg font-semibold text-slate-100">{title}</h3>
        {subtitle && <p className="text-sm text-subtle mt-1">{subtitle}</p>}
      </div>
      {action}
    </div>
  )
}
