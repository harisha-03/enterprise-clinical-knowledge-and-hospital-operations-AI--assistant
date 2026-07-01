import { motion } from 'framer-motion'
import { ArrowUpRight, ArrowDownRight } from 'lucide-react'
import { Card } from '../ui/Card.jsx'
import { useAnimatedCounter } from '../../hooks/useAnimatedCounter.js'

export default function KpiCard({ label, value, delta, icon: Icon, prefix = '', suffix = '', format }) {
  const animated = useAnimatedCounter(value, 1100)
  const isPositive = delta >= 0
  const display = format ? format(animated) : animated.toLocaleString('en-IN')

  return (
    <motion.div whileHover={{ y: -3 }} transition={{ duration: 0.15 }}>
      <Card hover className="p-6">
        <div className="flex items-start justify-between">
          <div>
            <p className="text-sm text-subtle font-medium">{label}</p>
            <p className="text-3xl font-bold text-slate-50 mt-2 tabular-nums tracking-tight">
              {prefix}{display}{suffix}
            </p>
          </div>
          <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center">
            <Icon size={22} className="text-primary-lighter" />
          </div>
        </div>
        {typeof delta === 'number' && (
          <div className="flex items-center gap-1.5 mt-4">
            {isPositive ? (
              <ArrowUpRight size={15} className="text-success" />
            ) : (
              <ArrowDownRight size={15} className="text-danger" />
            )}
            <span className={`text-sm font-medium ${isPositive ? 'text-success' : 'text-danger'}`}>
              {Math.abs(delta)}%
            </span>
            <span className="text-sm text-subtle">vs last month</span>
          </div>
        )}
      </Card>
    </motion.div>
  )
}
