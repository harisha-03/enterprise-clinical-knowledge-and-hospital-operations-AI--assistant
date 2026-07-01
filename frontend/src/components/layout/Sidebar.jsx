import { NavLink } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
  MessageSquareText, LayoutDashboard, Users, Stethoscope, CalendarClock,
  BedDouble, FlaskConical, Receipt, BarChart3, Settings as SettingsIcon,
  Activity, ChevronRight,
} from 'lucide-react'

const navItems = [
  { to: '/assistant', label: 'AI Assistant', icon: MessageSquareText },
  { to: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { to: '/patients', label: 'Patients', icon: Users },
  { to: '/doctors', label: 'Doctors', icon: Stethoscope },
  { to: '/appointments', label: 'Appointments', icon: CalendarClock },
  { to: '/admissions', label: 'Admissions', icon: BedDouble },
  { to: '/laboratory', label: 'Laboratory', icon: FlaskConical },
  { to: '/billing', label: 'Billing', icon: Receipt },
  { to: '/analytics', label: 'Analytics', icon: BarChart3 },
  { to: '/settings', label: 'Settings', icon: SettingsIcon },
]

export default function Sidebar() {
  return (
    <aside className="hidden md:flex md:w-[300px] shrink-0 flex-col border-r border-border bg-card/60 h-screen sticky top-0">
      <div className="flex items-center gap-3 px-6 h-24 border-b border-border">
        <div className="w-11 h-11 rounded-lg bg-primary flex items-center justify-center shadow-glow">
          <Activity size={19} className="text-white" />
        </div>
        <div className="leading-tight">
          <p className="text-lg font-semibold text-slate-100 tracking-tight">Clinical AI</p>
          <p className="text-xs text-subtle">Hospital Operations</p>
        </div>
      </div>

      <nav className="flex-1 overflow-y-auto py-5 px-4 space-y-1">
        <p className="px-3 pb-2 text-[11px] font-semibold uppercase tracking-wider text-subtle">Workspace</p>
        {navItems.map(({ to, label, icon: Icon }) => (
          <NavLink key={to} to={to} className="block">
            {({ isActive }) => (
              <motion.div
                whileHover={{ x: 2 }}
                transition={{ duration: 0.15 }}
                className={`group relative flex items-center gap-3 px-3.5 py-3 rounded-xl text-base font-medium transition-colors duration-150 ${
                  isActive
                    ? 'bg-primary/15 text-slate-50 border border-primary/30 shadow-glowSoft'
                    : 'text-muted hover:bg-white/5 hover:text-slate-100 border border-transparent'
                }`}
              >
                {isActive && (
                  <span className="absolute left-0 top-1/2 -translate-y-1/2 h-5 w-[3px] rounded-full bg-primary" />
                )}
                <Icon
                  size={19}
                  strokeWidth={2}
                  className={isActive ? 'text-primary-lighter' : 'text-subtle group-hover:text-slate-200 transition-colors'}
                />
                <span className="flex-1">{label}</span>
                {isActive && <ChevronRight size={15} className="text-primary-lighter/70" />}
              </motion.div>
            )}
          </NavLink>
        ))}
      </nav>

      <div className="p-4 border-t border-border">
        <div className="rounded-xl bg-cardsoft border border-border px-4 py-3.5">
          <p className="text-xs text-subtle font-medium">System status</p>
          <div className="flex items-center gap-2 mt-1.5">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-success opacity-60" />
              <span className="relative inline-flex rounded-full h-2 w-2 bg-success" />
            </span>
            <span className="text-[13px] text-slate-200 font-medium">All systems operational</span>
          </div>
        </div>
      </div>
    </aside>
  )
}
