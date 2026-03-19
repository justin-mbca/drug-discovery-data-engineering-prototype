import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders prototype title', () => {
  render(<App />);
  expect(screen.getByText(/Drug Discovery Data Engineering Prototype/i)).toBeInTheDocument();
});
