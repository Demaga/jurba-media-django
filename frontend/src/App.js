import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

export default function App() {
  const [articles, setArticles] = useState([]);
  
  useEffect(() => {
    fetch("http://localhost:8000/api/articles/published_articles/")
      .then((res) => {
        if (res.ok) {
          return res.json();
        }
        throw new Error("Couldn't fetch")
      })
      .then((data) => setArticles(data))
      .catch((error) => console.log(error))
  })

  return (
    <div className="App">
      <div className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h2>Welcome to React</h2>
      </div>
      {articles.map((article) => {
        <p>{article.title}</p>
      })}
    </div>
  );
  
}