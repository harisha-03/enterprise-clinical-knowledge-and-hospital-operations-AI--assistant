import axios from 'axios'

export const API_BASE_URL = 'http://127.0.0.1:8000'

export const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: { 'Content-Type': 'application/json' },
})

/**
 * Sends a question to the clinical AI assistant.
 * Backend contract:
 *  POST /ai/chat  { question: string }
 *  -> { intent, answer, sources: [{ document, page }] }
 */
export async function sendChatMessage(question) {
  const { data } = await api.post('/ai/chat', { question })
  return data
}
