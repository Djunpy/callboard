import React from "react";
import { NavLink, Link } from "react-router-dom";
import BellIcon from "../../assets/icons/bell-icon.svg";
import BookmarkIcon from "../../assets/icons/bookmark-icon.svg";
import ChatIcon from "../../assets/icons/chat-icon.svg";
import ProfileIcon from "../../assets/icons/profile-icon.svg";
import SearchIcon from "../../assets/icons/search-icon.svg";
import PluseIcon from "../../assets/icons/plus2.svg";
import PhotoIcon from "../../assets/icons/photo.svg";

const nav_link = [
    // {
    //     id: 1,
    //     title: "Найти обьявление",
    //     display: SearchIcon,
    //     path: "/bell",
    // },
    {
        id: 2,
        title: "Избранное",
        display: BookmarkIcon,
        path: "/bookmarks",
    },
    {
        id: 3,
        title: "Уведомления",
        display: BellIcon,
        path: "/bell",
    },
    {
        id: 4,
        title: "Сообщение",
        display: ChatIcon,
        path: "/chat",
    },

    {
        id: 6,
        title: "Профиль",
        display: ProfileIcon,
        path: "/profile",
    },
    // {
    //     id: 5,
    //     title: "Добавить обьявление",
    //     display: PluseIcon,
    //     path: "/bell",
    // },
];

const MobileHeader = () => {
    return (
        <div className="header-mobile block sm:hidden">
            <div className="header-mobile__box h-screen fixed top-0 left-0 w-3/4 bg-white z-50">
                <div className="header-mobile__top bg-second-dark-color flex items-center justify-center p-1">
                    <div className="header-mobil__img w-24 p-2 border-solid border-gray-300 border-[1px] rounded-full">
                        <img className="cover" src={PhotoIcon} alt="" />
                    </div>
                </div>
                <div className="header-list-icons space-y-5 p-4">
                    <Link to="/search" className="flex gap-x-5 shrink-0">
                        <img className="w-5" src={SearchIcon} alt="" />
                        <span>Найти обьявление</span>
                    </Link>
                    {nav_link.map((link) => (
                        <NavLink
                            key={link.id}
                            to={link.path}
                            className="flex items-center gap-x-5 p-1 shrink-0"
                        >
                            <div>
                                <img
                                    className="w-5 "
                                    src={link.display}
                                    alt=""
                                />
                            </div>
                            <span>{link.title}</span>
                        </NavLink>
                    ))}

                    <Link
                        to="/add-advert"
                        className="flex items-center gap-x-5 border-gray-300 border-solid border-[1px] border-l-0 border-r-0 p-1 shrink-0"
                    >
                        <div className="">
                            <img
                                className="w-6 border-[1px] rounded-full border-gray-300 border-solid"
                                src={PluseIcon}
                                alt=""
                            />
                        </div>
                        <span>Разместить обьявление</span>
                    </Link>
                    <div className="header-mobile__button flex flex-wrap items-center gap-2">
                        <Link to="/login">
                            <button className="p-1 bg-second-dark-color text-white hover:bg-primary-color hover:text-black transition-all rounded-md">
                                Войти
                            </button>
                        </Link>
                        <Link to="/register">
                            <button className="p-1 bg-second-dark-color text-white hover:bg-primary-color hover:text-black transition-all rounded-md">
                                Зарегистрироваться
                            </button>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MobileHeader;
