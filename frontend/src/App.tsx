import { useState, useEffect } from 'react'
import './App.css'

interface Habit {
  id: number
  name: string
  description: string
  completed: boolean
  created_at: string
  updated_at: string
}

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function App() {
  const [habits, setHabits] = useState<Habit[]>([])
  const [newHabitName, setNewHabitName] = useState('')
  const [newHabitDescription, setNewHabitDescription] = useState('')
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    fetchHabits()
  }, [])

  const fetchHabits = async () => {
    try {
      const response = await fetch(`${API_URL}/habits`)
      const data = await response.json()
      setHabits(data)
    } catch (error) {
      console.error('Error fetching habits:', error)
    }
  }

  const createHabit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!newHabitName.trim()) return

    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/habits`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: newHabitName,
          description: newHabitDescription,
        }),
      })
      const data = await response.json()
      setHabits([...habits, data])
      setNewHabitName('')
      setNewHabitDescription('')
    } catch (error) {
      console.error('Error creating habit:', error)
    } finally {
      setLoading(false)
    }
  }

  const toggleHabit = async (habitId: number) => {
    try {
      const response = await fetch(`${API_URL}/habits/${habitId}/toggle`, {
        method: 'PATCH',
      })
      const updatedHabit = await response.json()
      setHabits(habits.map(h => h.id === habitId ? updatedHabit : h))
    } catch (error) {
      console.error('Error toggling habit:', error)
    }
  }

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1>Habit Tracker</h1>
          <p>Track your daily habits and build better routines</p>
        </header>

        <form onSubmit={createHabit} className="habit-form">
          <div className="form-group">
            <input
              type="text"
              placeholder="Habit name"
              value={newHabitName}
              onChange={(e) => setNewHabitName(e.target.value)}
              className="input"
              disabled={loading}
            />
            <input
              type="text"
              placeholder="Description (optional)"
              value={newHabitDescription}
              onChange={(e) => setNewHabitDescription(e.target.value)}
              className="input"
              disabled={loading}
            />
          </div>
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? 'Adding...' : 'Add Habit'}
          </button>
        </form>

        <div className="habits-list">
          {habits.length === 0 ? (
            <p className="empty-message">No habits yet. Create your first habit above!</p>
          ) : (
            habits.map((habit) => (
              <div key={habit.id} className={`habit-card ${habit.completed ? 'completed' : ''}`}>
                <div className="habit-info">
                  <h3>{habit.name}</h3>
                  {habit.description && <p>{habit.description}</p>}
                </div>
                <button
                  onClick={() => toggleHabit(habit.id)}
                  className={`btn ${habit.completed ? 'btn-success' : 'btn-secondary'}`}
                >
                  {habit.completed ? '✓ Done' : 'Mark Done'}
                </button>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  )
}

export default App
