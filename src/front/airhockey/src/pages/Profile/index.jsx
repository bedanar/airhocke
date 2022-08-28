import React from "react";
import Header from "../../components/Header";
import { Popover} from '@headlessui/react'
import Profile from "../../components/Profile/Profile";

const ProfilePage = () => {
    return (
        <Popover className="relative z-10">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 z-10">
                <Header isAuth={true} />
                <Profile />
            </div>
        </Popover>
    )
}
export default ProfilePage