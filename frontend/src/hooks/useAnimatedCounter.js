import { useEffect, useRef, useState } from 'react'

/**
 * Animates a numeric value from 0 to `target` over `duration` ms.
 */
export function useAnimatedCounter(target = 0, duration = 1000) {
  const [value, setValue] = useState(0)
  const startRef = useRef(null)
  const frameRef = useRef(null)

  useEffect(() => {
    startRef.current = null
    cancelAnimationFrame(frameRef.current)

    function step(timestamp) {
      if (startRef.current === null) startRef.current = timestamp
      const progress = Math.min((timestamp - startRef.current) / duration, 1)
      const eased = 1 - Math.pow(1 - progress, 3)
      setValue(Math.floor(eased * target))
      if (progress < 1) {
        frameRef.current = requestAnimationFrame(step)
      } else {
        setValue(target)
      }
    }

    frameRef.current = requestAnimationFrame(step)
    return () => cancelAnimationFrame(frameRef.current)
  }, [target, duration])

  return value
}
