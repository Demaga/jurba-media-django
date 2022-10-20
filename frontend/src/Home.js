// import styles from "../styles/ArticleCard.module.css";
import React, { useState, useEffect } from 'react';

export default function Home(props) {
  const [articles, setArticles] = useState([]);
  
  useEffect(() => {
    fetch("http://localhost:8000/api/articles/published_articles/")
      .then((res) => {
        if (res.ok) {
          return res.json();
        }
        throw new Error("Couldn't fetch")
      })
      .then((data) =>  setArticles(data))
      .catch((error) => console.log(error));
  }, [])
  
  console.log(articles);
  return (
    <div className="articles-list">
      {articles.map((article) => {
        return (
          <div class="article">
            <p>{article.id}</p>
            <p>{article.title}</p>
          </div>
        )
      })}
    </div>
  );
}
