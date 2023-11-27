import { render, screen } from '@testing-library/react';
import UserRegistration from '../UserRegistration';

test('renders UserRegistration component', () => {
  render(<UserRegistration />);
  const linkElement = screen.getByText(/First Name:/i);
  expect(linkElement).toBeInTheDocument();
});