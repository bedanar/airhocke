import React from "react";
import { Tab } from "../Tab";
import styles from './Profile.module.scss'
import star from '../../assets/img/star.png'
import image from '../../assets/img/image.png'

const data = 
    {
        image: image,
        rating: 1,
        username: 'dweebishqys',
        stars: 5,
        gamesAll: 1234,
        gamesWon: 1000,
        gamesLost: 234,
        gamesInfo: [
            {
                id: 1,
                number: 12345,
                date: '30.07.2022',
                opponent: 'desalotAge',
                score: '3:4',
                winner: 'dweebishqys'
            },
            {
                id: 2,
                number: 12345,
                date: '30.07.2022',
                opponent: 'desalotAge',
                score: '3:4',
                winner: 'dweebishqys'
            },
            {
                id: 3,
                number: 12345,
                date: '30.07.2022',
                opponent: 'desalotAge',
                score: '3:4',
                winner: 'dweebishqys'
            },
            {
                id: 4,
                number: 12345,
                date: '30.07.2022',
                opponent: 'desalotAge',
                users: 3,
                oponnets: 4,
                winner: 'dweebishqys'
            },
        ]
    }


const Profile = () => {
    const ss = []
    for (let i = 0; i < data.stars; i++) {
        ss[i] = i+1;
    }
    return (
        <div className={styles.profile}>
            <div className={styles.profile__information}>
                <div className={styles.profile__image}>
                    <img src={data.image} alt="profile image" />
                    <span className={styles.profile__rating}>#{data.rating}</span>
                </div>
                <p className={styles.profile__username}>@{data.username}</p>
                <div className={styles.profile__stars}>
                    {
                        ss.map((_, ind) => <div key={ind} className={styles.profile__star}>
                            <img src={star} alt='star' key={ind} />
                        </div>)
                    }
                </div>
                <div className={styles.profile__games}> {data.gamesAll} games | {data.gamesWon} wins | {data.gamesLost} failures | №{data.rating} in raiting</div>
                <button className={styles.profile__inviteBtn}>invite to play</button>
            </div>
            <Tab />
        </div>
    )
}
export default Profile