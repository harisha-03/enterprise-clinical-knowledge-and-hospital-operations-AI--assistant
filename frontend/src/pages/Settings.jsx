import { useState } from 'react'
import { Settings as SettingsIcon, Bell, Shield, Palette, Database, Check } from 'lucide-react'
import { Card, CardHeader } from '../components/ui/Card.jsx'
import Button from '../components/ui/Button.jsx'

function Toggle({ enabled, onChange }) {
  return (
    <button
      onClick={() => onChange(!enabled)}
      className={`w-10 h-6 rounded-full relative transition-colors duration-150 ${enabled ? 'bg-primary' : 'bg-border'}`}
    >
      <span
        className={`absolute top-0.5 left-0.5 w-5 h-5 rounded-full bg-white transition-transform duration-150 ${
          enabled ? 'translate-x-4' : 'translate-x-0'
        }`}
      />
    </button>
  )
}

export default function Settings() {
  const [notifications, setNotifications] = useState(true)
  const [emailAlerts, setEmailAlerts] = useState(true)
  const [twoFactor, setTwoFactor] = useState(false)
  const [saved, setSaved] = useState(false)

  function handleSave() {
    setSaved(true)
    setTimeout(() => setSaved(false), 2000)
  }

  return (
    <div className="p-6 md:p-8 space-y-6 max-w-3xl">
      <div className="flex items-center gap-2.5">
        <div className="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center">
          <SettingsIcon size={17} className="text-primary-light" />
        </div>
        <div>
          <p className="text-sm font-semibold text-slate-100">Settings</p>
          <p className="text-xs text-subtle">Manage your workspace preferences</p>
        </div>
      </div>

      <Card>
        <CardHeader title="API Connection" subtitle="Backend used by the AI Assistant" />
        <div className="px-5 pb-5 flex items-center gap-3">
          <Database size={16} className="text-primary-light" />
          <code className="text-sm text-slate-300 bg-bg border border-border rounded-md px-3 py-1.5">
            http://127.0.0.1:8000
          </code>
          <span className="flex items-center gap-1.5 text-xs text-success">
            <span className="w-1.5 h-1.5 rounded-full bg-success animate-pulseSoft" /> Connected
          </span>
        </div>
      </Card>

      <Card>
        <CardHeader title="Notifications" subtitle="Choose what you want to be notified about" />
        <div className="px-5 pb-5 space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2.5">
              <Bell size={15} className="text-subtle" />
              <span className="text-sm text-slate-200">Push notifications</span>
            </div>
            <Toggle enabled={notifications} onChange={setNotifications} />
          </div>
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2.5">
              <Bell size={15} className="text-subtle" />
              <span className="text-sm text-slate-200">Email alerts for critical events</span>
            </div>
            <Toggle enabled={emailAlerts} onChange={setEmailAlerts} />
          </div>
        </div>
      </Card>

      <Card>
        <CardHeader title="Security" />
        <div className="px-5 pb-5">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2.5">
              <Shield size={15} className="text-subtle" />
              <span className="text-sm text-slate-200">Two-factor authentication</span>
            </div>
            <Toggle enabled={twoFactor} onChange={setTwoFactor} />
          </div>
        </div>
      </Card>

      <Card>
        <CardHeader title="Appearance" subtitle="Theme used across the platform" />
        <div className="px-5 pb-5 flex items-center gap-2.5">
          <Palette size={15} className="text-subtle" />
          <span className="text-sm text-slate-200">Dark theme</span>
          <span className="text-xs text-subtle">(default, locked for clinical environments)</span>
        </div>
      </Card>

      <Button onClick={handleSave} icon={saved ? Check : undefined}>
        {saved ? 'Saved' : 'Save Changes'}
      </Button>
    </div>
  )
}
