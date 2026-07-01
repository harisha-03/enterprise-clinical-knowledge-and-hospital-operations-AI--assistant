/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        bg: '#0A0F1C',
        card: '#111827',
        cardhover: '#161F2E',
        cardsoft: '#0D1420',
        border: '#1E293B',
        borderlight: '#263349',
        primary: {
          DEFAULT: '#2563EB',
          light: '#3B82F6',
          lighter: '#60A5FA',
          dark: '#1D4ED8',
          soft: '#1E3A8A',
        },
        success: '#10B981',
        warning: '#F59E0B',
        danger: '#EF4444',
        muted: '#94A3B8',
        subtle: '#64748B',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      fontSize: {
        xs: ['12.5px', { lineHeight: '1.5' }],
        sm: ['14px', { lineHeight: '1.55' }],
        base: ['16px', { lineHeight: '1.65' }],
        md: ['17px', { lineHeight: '1.65' }],
        lg: ['18px', { lineHeight: '1.7' }],
        xl: ['20px', { lineHeight: '1.5' }],
        '2xl': ['24px', { lineHeight: '1.35' }],
        '3xl': ['28px', { lineHeight: '1.3' }],
        '4xl': ['32px', { lineHeight: '1.25' }],
      },
      maxWidth: {
        chat: '1360px',
      },
      boxShadow: {
        card: '0 1px 2px 0 rgba(0,0,0,0.35), 0 1px 3px 0 rgba(0,0,0,0.25)',
        elevated: '0 4px 16px -4px rgba(0,0,0,0.4), 0 2px 6px -2px rgba(0,0,0,0.3)',
        glow: '0 0 0 1px rgba(37,99,235,0.3), 0 8px 24px -4px rgba(37,99,235,0.25)',
        glowSoft: '0 0 0 1px rgba(37,99,235,0.15), 0 4px 14px -4px rgba(37,99,235,0.2)',
      },
      keyframes: {
        pulseSoft: {
          '0%, 100%': { opacity: 1 },
          '50%': { opacity: 0.5 },
        },
        shimmer: {
          '0%': { backgroundPosition: '-400px 0' },
          '100%': { backgroundPosition: '400px 0' },
        },
        fadeInUp: {
          '0%': { opacity: 0, transform: 'translateY(6px)' },
          '100%': { opacity: 1, transform: 'translateY(0)' },
        },
      },
      animation: {
        pulseSoft: 'pulseSoft 1.6s ease-in-out infinite',
        shimmer: 'shimmer 1.8s linear infinite',
        fadeInUp: 'fadeInUp 0.25s ease-out',
      },
    },
  },
  plugins: [],
}
