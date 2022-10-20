import styles from './Layout.css'


export default function Layout({ children }) {
  return (
    <>
      <nav className={styles.nav}>
        <div className="content">
          <span className={styles.title}>Журба</span>
        </div>
      </nav>

      <main className="content">{children}</main>

      <footer className={styles.footer}>
        <div className="content">
          <p>Тут буде футер</p>
        </div>
      </footer>
    </>
  )
}