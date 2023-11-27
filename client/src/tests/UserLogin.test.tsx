/**
 * @jest-environment jsdom
 */

import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import UserLogin from '../UserLogin';

describe('UserLogin', () => {
  test('fills out the form and clicks the login button', () => {
    const { getByPlaceholderText, getByText } = render(
      <Router>
        <UserLogin />
      </Router>
    );

    // Fill out the form
    fireEvent.change(getByPlaceholderText('Username'), { target: { value: 'testuser' } });
    fireEvent.change(getByPlaceholderText('Password'), { target: { value: 'testpass' } });

    // Click the Login button
    fireEvent.click(getByText('Login'));

    // Check that the form fields were filled correctly
    expect((getByPlaceholderText('Username') as HTMLInputElement).value).toBe('testuser');
    expect((getByPlaceholderText('Password') as HTMLInputElement).value).toBe('testpass');
  });
});