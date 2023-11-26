// Button that we can use for alll the pages for standardized design
import React from 'react';
import './Button.css';

interface ButtonProps {
  href?: string;
  children: React.ReactNode;
  onClick?: (event: React.MouseEvent<HTMLButtonElement | HTMLAnchorElement, MouseEvent>) => void;
}

const Button: React.FC<ButtonProps> = ({ href, children, onClick }) => { 
  if (href) {
    return (
      <a className="btn" href={href} onClick={onClick}>{children}</a>
    );
  } else {
    return (
      <button className="btn" type="submit" onClick={onClick}>{children}</button>
    );
  }
};

export default Button;