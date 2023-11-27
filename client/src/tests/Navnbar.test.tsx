import { render, screen } from '@testing-library/react';
import Navbar from '../Navbar';

test('renders Navbar component', () => {
  render(<Navbar />);
  const linkElement = screen.getByText(/Home/i);
  expect(linkElement).toBeInTheDocument();
});