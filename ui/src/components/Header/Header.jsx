import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import Logo from "../../assets/img/logo.png";
import SearchIcon from "../../assets/icons/search-icon.svg";
import ChatIcon from "../../assets/icons/chat-icon.svg";
import ProfileIcon from "../../assets/icons/profile-icon.svg";
import BellIcon from "../../assets/icons/bell-icon.svg";
import BookmarkIcon from "../../assets/icons/bookmark-icon.svg";
import CategoryIcon2 from "../../assets/icons/categroy2.svg";
import PlusAdsIcon from "../../assets/icons/plus2.svg";
import { Category } from "../UI/Category/Category";
import MobileHeader from "./MobileHeader";
import MenuIcon from "../../assets/icons/menu.svg";

const nav_link = [
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
];

export const Header = () => {
    const [mobileSearch, setMobileSearch] = useState(false);
    const [dropdownVisible, setDropdownVisible] = useState(null);
    const [mainHeaderFixed, setMainHeaderFixed] = useState(false);
    const showDropdown = () => {
        setDropdownVisible(!dropdownVisible);
    };

    const mobileSearchToggle = () => {
        setMobileSearch(!mobileSearch);
    };
    const mainHeaderToggle = () => {
        if (window.scrollY >= 10) {
            setMainHeaderFixed(true);
        } else if (window.scrollY <= 10) {
            setMainHeaderFixed(false);
        }
    };

    useEffect(() => {
        window.addEventListener("scroll", mainHeaderToggle);
    }, []);

    return (
        <header className="header ">
            <div className="header-container relative">
                <div className="header-top">
                    <div className="header-top-wrapp">
                        <ul className="header-top_list ">
                            <li className="custom-hover">FAQ</li>
                            <li className="custom-hover">
                                <a href="mailto:vlad@htmlbook.ru">
                                    Напишите нам
                                </a>
                            </li>
                        </ul>
                        <div className="header-search hidden sm:flex lg:hidden">
                            <p className="search-wrapp ">
                                <input
                                    className="search__input"
                                    type="search"
                                    placeholder="Найти товар"
                                />
                                <img src={SearchIcon} alt="Иконка поиска" />
                                <select className="search-select">
                                    <option>Выбрать регион</option>
                                    <option value="md">Молдова</option>
                                    <option value="pmr">Приднестровье</option>
                                </select>
                            </p>
                            <button className="search-btn primary-hover">
                                Поиск
                            </button>
                        </div>

                        <div className="order-2 ">
                            <button className="header-top_btn hidden">
                                Разместить обьявление
                            </button>
                            <button className="top-second_btn ">
                                <img src={PlusAdsIcon} alt="" />
                            </button>
                        </div>
                        <div className="w-20 block sm:hidden">
                            <img src={Logo} alt="" />
                        </div>
                    </div>
                </div>
                <div
                    className={`header-main ${
                        mainHeaderFixed ? "main-header-fixed" : "static"
                    } `}
                >
                    <div className="header-main_wrapp">
                        <div className="header-logo hidden sm:block">
                            <img src={Logo} alt="Логотип сайта" />
                        </div>
                        <div className="header-category">
                            <div className="category-icon relative group/category-icon">
                                <button className=" icons">
                                    <img
                                        src={CategoryIcon2}
                                        alt="Иконка категорий"
                                    />
                                    <span>Категории</span>
                                </button>
                                <Category
                                    dropdownVisible={dropdownVisible}
                                    showDropdown={showDropdown}
                                />
                            </div>
                        </div>
                        <div className="header-search hidden lg:flex">
                            <p className="search-wrapp">
                                <input
                                    className="search__input"
                                    type="search"
                                    placeholder="Найти товар"
                                />
                                <img src={SearchIcon} alt="Иконка поиска" />
                                <select name="" id="" className="search-select">
                                    <option>Выбрать регион</option>
                                    <option value="md">Молдова</option>
                                    <option value="pmr">Приднестровье</option>
                                </select>
                            </p>
                            <button className="search-btn hover:text-white">
                                Поиск
                            </button>
                        </div>
                        <div
                            className={`header-search__mobile ${
                                mobileSearch ? "show" : "hidden"
                            }`}
                        >
                            <p>
                                <input
                                    className="search__input rounded-full"
                                    type="search"
                                    placeholder="Поиск.."
                                />
                                <button className="search-mobile__btn">
                                    Найти
                                </button>
                            </p>
                        </div>
                        <div className="main-icons">
                            <ul className="main-icon_list">
                                <li
                                    className="main-list_item block sm:hidden"
                                    onClick={mobileSearchToggle}
                                >
                                    <img
                                        src={SearchIcon}
                                        alt="Иконка личных сообщений"
                                    />
                                </li>
                                <li className="main-list_item block sm:hidden">
                                    <img src={MenuIcon} alt="" />
                                </li>
                                {nav_link.map((link) => (
                                    <NavLink
                                        className="main-list_item hidden sm:block"
                                        key={link.id}
                                        to={link.path}
                                    >
                                        <img src={link.display} alt="" />
                                        <span>1</span>
                                    </NavLink>
                                ))}
                                <li className="main-list_item hidden sm:block">
                                    <img
                                        src={ProfileIcon}
                                        alt="Иконка профиля"
                                    />
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <MobileHeader />
            </div>
        </header>
    );
};
