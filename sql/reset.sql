-- Example items.sql

-- Create database "demo"
CREATE DATABASE IF NOT EXISTS demo;
USE demo;

-- Create items table
CREATE TABLE items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Insert sample data
INSERT INTO items (name) 
VALUES 
  ('Laptop'),
  ('Phone'),
  ('Tablet'),
  ('Headphones'),
  ('Keyboard');