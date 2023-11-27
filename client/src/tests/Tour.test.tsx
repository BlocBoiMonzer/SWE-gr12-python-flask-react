import { render, screen } from '@testing-library/react';
import SingleTour from '../SingleTour';
import TourList from '../TourList';

test('renders SingleTour component', () => {
  render(<SingleTour tour={{id: 1, name: 'Test Tour', description: 'Test Description'}} />);
  const linkElement = screen.getByText(/Test Tour/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders TourList component', () => {
  render(<TourList />);
  const linkElement = screen.getByText(/Loading.../i);
  expect(linkElement).toBeInTheDocument();
});