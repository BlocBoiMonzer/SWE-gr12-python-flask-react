import '@testing-library/jest-dom/extend-expect';
import { render, screen } from '@testing-library/react';
import UserProfile from '../UserProfile';

test('renders UserProfile component', () => {
  render(<UserProfile />);
  const linkElement = screen.getByText(/Loading.../i);
  expect(linkElement).toBeDefined();
});