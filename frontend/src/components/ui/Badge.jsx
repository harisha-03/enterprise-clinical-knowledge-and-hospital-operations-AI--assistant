const variants = {
  success: 'bg-success/15 text-success border-success/30',
  warning: 'bg-warning/15 text-warning border-warning/30',
  danger: 'bg-danger/15 text-danger border-danger/30',
  primary: 'bg-primary/15 text-primary-light border-primary/30',
  neutral: 'bg-white/5 text-muted border-border',
}

export default function Badge({ children, variant = 'neutral', className = '' }) {
  return (
    <span
      className={`inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium border ${variants[variant]} ${className}`}
    >
      {children}
    </span>
  )
}

export function statusVariant(status) {
  const s = status?.toLowerCase() || ''
  if (['admitted', 'confirmed', 'completed', 'paid', 'available'].includes(s)) return 'success'
  if (['pending', 'processing', 'under observation', 'outpatient'].includes(s)) return 'warning'
  if (['cancelled', 'critical', 'overdue', 'on leave'].includes(s)) return 'danger'
  return 'neutral'
}
