import { useState, useEffect } from 'react';
import './App.css';

interface Habit {
  id: number;
  name: string;
  description: string;
  completed: boolean;
  created_at: string;
}

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [habits, setHabits] = useState<Habit[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [newHabitName, setNewHabitName] = useState('');
  const [newHabitDescription, setNewHabitDescription] = useState('');

  useEffect(() => {
    fetchHabits();
  }, []);

  const fetchHabits = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_URL}/habits/`);
      if (!response.ok) {
        throw new Error('Failed to fetch habits');
      }
      const data = await response.json();
      setHabits(data);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const createHabit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newHabitName.trim()) return;

    try {
      const response = await fetch(`${API_URL}/habits/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: newHabitName,
          description: newHabitDescription,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to create habit');
      }

      const newHabit = await response.json();
      setHabits([...habits, newHabit]);
      setNewHabitName('');
      setNewHabitDescription('');
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to create habit');
    }
  };

  const toggleHabit = async (id: number) => {
    try {
      const response = await fetch(`${API_URL}/habits/${id}/toggle`, {
        method: 'PUT',
      });

      if (!response.ok) {
        throw new Error('Failed to toggle habit');
      }

      const updatedHabit = await response.json();
      setHabits(habits.map(h => (h.id === id ? updatedHabit : h)));
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to toggle habit');
    }
  };

  const deleteHabit = async (id: number) => {
    try {
      const response = await fetch(`${API_URL}/habits/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete habit');
      }

      setHabits(habits.filter(h => h.id !== id));
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete habit');
    }
  };

  return (
    <div className="app-container">
      <div className="app-header">
        <h1>Habit Tracker</h1>
        <p>Build better habits, one day at a time</p>
      </div>

      {error && <div className="error">{error}</div>}

      <form className="habit-form" onSubmit={createHabit}>
        <input
          type="text"
          placeholder="Habit name (e.g., Exercise)"
          value={newHabitName}
          onChange={(e) => setNewHabitName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Description (optional)"
          value={newHabitDescription}
          onChange={(e) => setNewHabitDescription(e.target.value)}
        />
        <button type="submit" disabled={!newHabitName.trim()}>
          Add Habit
        </button>
      </form>

      {loading ? (
        <div className="loading">Loading habits...</div>
      ) : habits.length === 0 ? (
        <div className="empty-state">
          <h3>No habits yet</h3>
          <p>Start by adding your first habit above!</p>
        </div>
      ) : (
        <div className="habits-list">
          {habits.map((habit) => (
            <div
              key={habit.id}
              className={`habit-item ${habit.completed ? 'completed' : ''}`}
            >
              <div className="habit-info">
                <h3>{habit.name}</h3>
                {habit.description && <p>{habit.description}</p>}
              </div>
              <div className="habit-actions">
                <button
                  className={`toggle-btn ${habit.completed ? 'completed' : ''}`}
                  onClick={() => toggleHabit(habit.id)}
                >
                  {habit.completed ? '✓ Done' : 'Mark Done'}
                </button>
                <button
                  className="delete-btn"
                  onClick={() => deleteHabit(habit.id)}
                >
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
