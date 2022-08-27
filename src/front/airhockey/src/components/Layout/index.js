import React from "react";
import styles from './Layout.module.scss'

const Layout = ({children}) => {
    return (
        <div className={styles.bg}>
            <div className={styles.layout}>{children}</div>
        </div>
    )
}

export default Layout