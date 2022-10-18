// import styles from "../styles/ArticleCard.module.css";

export default function ArticleCard(props) {
  const article = props.article;
  
  return (
    <div>
      <img src={article.image} />
      <p>
        <b>{article.title}</b>. {article.subtitle}
      </p>
    </div>
  );
}
