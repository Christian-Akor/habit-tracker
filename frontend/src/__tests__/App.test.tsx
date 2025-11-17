import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import App from '../App'

describe('App', () => {
  it('renders the app title', () => {
    render(<App />)
    expect(screen.getByText('Habit Tracker')).toBeInTheDocument()
  })

  it('renders the subtitle', () => {
    render(<App />)
    expect(screen.getByText('Track your daily habits and build better routines')).toBeInTheDocument()
  })

  it('renders the add habit button', () => {
    render(<App />)
    expect(screen.getByRole('button', { name: /add habit/i })).toBeInTheDocument()
  })

  it('renders empty message when no habits exist', () => {
    render(<App />)
    expect(screen.getByText(/no habits yet/i)).toBeInTheDocument()
  })
})
