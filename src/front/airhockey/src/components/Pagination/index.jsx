import React, { useState } from "react";
import { Arrow } from "../../assets/img/icons";
import styles from './Pagination.module.scss'

const Pagination = ({color, numbers}) => {
    const [isActive, setIsActive] = useState(1)
    const ns = []
    for (let i = 0; i < numbers; i++) {
        ns[i] = i+1
    }
    const handleForward = (ind) => {
        setIsActive(ind + 1)
    }
    const handleBackward = (ind) => {
        setIsActive(ind - 1)
    }
    return (
        <div className={styles.pagination}>
            <button className={styles.arrow__left} onClick={() => handleBackward(isActive)}>
                <Arrow />
            </button>
            <div className={styles.pagination__pages}>
                {
                    ns.map((n, index) => {
                        return (
                            <button key={index} className={isActive === index ? styles.pagination__itemActive : styles.pagination__item} onClick={() => setIsActive(index)}>{n}</button>
                        )
                    })
                }
            </div>
            <button className={styles.arrow__right} onClick={() => handleForward(isActive)}>
                <Arrow />
            </button>
        </div>
    )
}
export default Pagination