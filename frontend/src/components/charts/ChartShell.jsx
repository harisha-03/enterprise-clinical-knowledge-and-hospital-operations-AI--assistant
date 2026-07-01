import { Card, CardHeader } from '../ui/Card.jsx'

export default function ChartShell({ title, subtitle, action, children, className = '' }) {
  return (
    <Card className={className}>
      <CardHeader title={title} subtitle={subtitle} action={action} />
      <div className="px-3 pb-4">{children}</div>
    </Card>
  )
}

export const chartTooltipStyle = {
  contentStyle: {
    background: '#111827',
    border: '1px solid #1F2937',
    borderRadius: 8,
    fontSize: 12,
    color: '#E5E7EB',
  },
  labelStyle: { color: '#94A3B8' },
}
