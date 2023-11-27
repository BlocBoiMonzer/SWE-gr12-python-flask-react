import { render } from '@testing-library/react';
import Logout from '../Logout';

test('renders Logout component', () => {
  const { container } = render(<Logout />);
  expect(container).toBeEmpty();
});