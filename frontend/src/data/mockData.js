// Mock data used to populate the operational dashboards.
// Replace with real API calls once those endpoints are available.

export const kpis = {
  patients: { value: 4218, delta: 4.6 },
  doctors: { value: 186, delta: 1.2 },
  appointments: { value: 312, delta: -2.4 },
  admissions: { value: 58, delta: 7.8 },
  revenue: { value: 1284600, delta: 9.1 },
  beds: { value: 412, occupied: 327 },
}

export const admissionsTrend = [
  { month: 'Jan', admissions: 210, discharges: 198 },
  { month: 'Feb', admissions: 244, discharges: 220 },
  { month: 'Mar', admissions: 268, discharges: 251 },
  { month: 'Apr', admissions: 231, discharges: 240 },
  { month: 'May', admissions: 290, discharges: 265 },
  { month: 'Jun', admissions: 312, discharges: 288 },
  { month: 'Jul', admissions: 334, discharges: 301 },
]

export const revenueTrend = [
  { month: 'Jan', revenue: 820000, expenses: 610000 },
  { month: 'Feb', revenue: 865000, expenses: 625000 },
  { month: 'Mar', revenue: 910000, expenses: 640000 },
  { month: 'Apr', revenue: 940000, expenses: 655000 },
  { month: 'May', revenue: 1020000, expenses: 690000 },
  { month: 'Jun', revenue: 1150000, expenses: 720000 },
  { month: 'Jul', revenue: 1284600, expenses: 745000 },
]

export const departmentDistribution = [
  { name: 'Cardiology', value: 24, color: '#2563EB' },
  { name: 'Neurology', value: 18, color: '#10B981' },
  { name: 'Orthopedics', value: 16, color: '#F59E0B' },
  { name: 'Pediatrics', value: 14, color: '#EF4444' },
  { name: 'Oncology', value: 12, color: '#8B5CF6' },
  { name: 'General', value: 16, color: '#06B6D4' },
]

export const bedOccupancy = [
  { ward: 'ICU', total: 40, occupied: 36 },
  { ward: 'General', total: 220, occupied: 168 },
  { ward: 'Maternity', total: 60, occupied: 41 },
  { ward: 'Pediatric', total: 50, occupied: 33 },
  { ward: 'Emergency', total: 42, occupied: 38 },
]

export const recentActivity = [
  { id: 1, type: 'admission', text: 'Patient Ananya Rao admitted to Cardiology', time: '6 min ago' },
  { id: 2, type: 'discharge', text: 'Patient Vikram Shah discharged from General Ward', time: '22 min ago' },
  { id: 3, type: 'lab', text: 'Lab results ready for Patient ID #4821', time: '38 min ago' },
  { id: 4, type: 'appointment', text: 'Dr. Meera Iyer booked for 3 new appointments', time: '1 hr ago' },
  { id: 5, type: 'billing', text: 'Invoice #INV-2291 marked as paid', time: '2 hr ago' },
]

export const patients = Array.from({ length: 48 }).map((_, i) => ({
  id: `PT-${2000 + i}`,
  name: ['Ananya Rao', 'Vikram Shah', 'Priya Nair', 'Rohit Verma', 'Kavya Reddy', 'Arjun Mehta', 'Sneha Joshi', 'Karthik Pillai'][i % 8],
  age: 18 + (i % 60),
  gender: i % 2 === 0 ? 'Female' : 'Male',
  department: ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Oncology', 'General'][i % 6],
  status: ['Admitted', 'Discharged', 'Outpatient', 'Critical'][i % 4],
  lastVisit: `2026-0${(i % 6) + 1}-${String((i % 27) + 1).padStart(2, '0')}`,
}))

export const doctors = Array.from({ length: 24 }).map((_, i) => ({
  id: `DR-${100 + i}`,
  name: ['Dr. Meera Iyer', 'Dr. Aman Gupta', 'Dr. Sara Khan', 'Dr. Nikhil Bose', 'Dr. Divya Menon', 'Dr. Rajesh Kumar'][i % 6],
  department: ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Oncology', 'General'][i % 6],
  patients: 20 + (i % 40),
  rating: (4 + (i % 10) / 10).toFixed(1),
  status: i % 5 === 0 ? 'On Leave' : 'Available',
}))

export const appointments = Array.from({ length: 30 }).map((_, i) => ({
  id: `AP-${5000 + i}`,
  patient: patients[i % patients.length].name,
  doctor: doctors[i % doctors.length].name,
  date: `2026-07-${String((i % 27) + 1).padStart(2, '0')}`,
  time: `${9 + (i % 8)}:00`,
  status: ['Confirmed', 'Pending', 'Completed', 'Cancelled'][i % 4],
}))

export const admissionsList = Array.from({ length: 26 }).map((_, i) => ({
  id: `AD-${3000 + i}`,
  patient: patients[i % patients.length].name,
  ward: ['ICU', 'General', 'Maternity', 'Pediatric', 'Emergency'][i % 5],
  admittedOn: `2026-06-${String((i % 27) + 1).padStart(2, '0')}`,
  doctor: doctors[i % doctors.length].name,
  status: ['Admitted', 'Under Observation', 'Discharged'][i % 3],
}))

export const labTests = Array.from({ length: 22 }).map((_, i) => ({
  id: `LB-${7000 + i}`,
  patient: patients[i % patients.length].name,
  test: ['CBC Panel', 'Lipid Profile', 'Liver Function', 'Dengue NS1', 'Thyroid Panel', 'X-Ray Chest'][i % 6],
  status: ['Completed', 'Processing', 'Pending'][i % 3],
  date: `2026-06-${String((i % 27) + 1).padStart(2, '0')}`,
}))

export const invoices = Array.from({ length: 20 }).map((_, i) => ({
  id: `INV-${2200 + i}`,
  patient: patients[i % patients.length].name,
  amount: 1500 + i * 340,
  status: ['Paid', 'Pending', 'Overdue'][i % 3],
  date: `2026-06-${String((i % 27) + 1).padStart(2, '0')}`,
}))
