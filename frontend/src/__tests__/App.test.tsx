import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import App from '../App';

describe('App', () => {
  it('renders the app title', () => {
    render(<App />);
    expect(screen.getByText('Habit Tracker')).toBeDefined();
  });

  it('renders the subtitle', () => {
    render(<App />);
    expect(screen.getByText('Build better habits, one day at a time')).toBeDefined();
  });

  it('renders the add habit button', () => {
    render(<App />);
    expect(screen.getByText('Add Habit')).toBeDefined();
  });

  it('renders habit name input field', () => {
    render(<App />);
    expect(screen.getByPlaceholderText(/Habit name/i)).toBeDefined();
  });
});
