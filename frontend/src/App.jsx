import { Routes, Route, Navigate } from 'react-router-dom'
import MainLayout from './components/layout/MainLayout.jsx'
import Dashboard from './pages/Dashboard.jsx'
import Assistant from './pages/Assistant.jsx'
import Patients from './pages/Patients.jsx'
import Doctors from './pages/Doctors.jsx'
import Appointments from './pages/Appointments.jsx'
import Admissions from './pages/Admissions.jsx'
import Laboratory from './pages/Laboratory.jsx'
import Billing from './pages/Billing.jsx'
import Analytics from './pages/Analytics.jsx'
import Settings from './pages/Settings.jsx'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<MainLayout />}>
        <Route index element={<Navigate to="/assistant" replace />} />
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="assistant" element={<Assistant />} />
        <Route path="patients" element={<Patients />} />
        <Route path="doctors" element={<Doctors />} />
        <Route path="appointments" element={<Appointments />} />
        <Route path="admissions" element={<Admissions />} />
        <Route path="laboratory" element={<Laboratory />} />
        <Route path="billing" element={<Billing />} />
        <Route path="analytics" element={<Analytics />} />
        <Route path="settings" element={<Settings />} />
        <Route path="*" element={<Navigate to="/assistant" replace />} />
      </Route>
    </Routes>
  )
}
