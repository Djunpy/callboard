import React, { useState, useEffect } from "react";
import Logo from "../../assets/img/logo.png";
import SearchIcon from "../../assets/icons/search-icon.svg";
import ChatIcon from "../../assets/icons/chat-icon.svg";
import ProfileIcon from "../../assets/icons/profile-icon.svg";
import BellIcon from "../../assets/icons/bell-icon.svg";
import BookmarkIcon from "../../assets/icons/bookmark-icon.svg";
import CategoryIcon2 from "../../assets/icons/categroy2.svg";
import PlusAdsIcon from "../../assets/icons/plus2.svg";
import { Category } from "../UI/Category/Category";

export const Header = () => {
    const [dropdownVisible, setDropdownVisible] = useState(null);
    const [mainHeaderFixed, setMainHeaderFixed] = useState(false);
    const showDropdown = () => {
        setDropdownVisible(!dropdownVisible);
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
                        <div className="header-search flex lg:hidden">
                            <p className="search-wrapp ">
                                <input
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
                            <button className="search-btn primary-hover">
                                Поиск
                            </button>
                        </div>
                        <div>
                            <button className="header-top_btn hidden">
                                Разместить обьявление
                            </button>
                            <button className="top-second_btn">
                                <img src={PlusAdsIcon} alt="" />
                            </button>
                        </div>
                    </div>
                </div>
                <div
                    className={`header-main ${
                        mainHeaderFixed ? "main-header-fixed" : "static"
                    }`}
                >
                    <div className="header-main_wrapp">
                        <div className="header-logo">
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
                        <div className="main-icons">
                            <ul className="main-icon_list">
                                <li className="main-list_item search-icon">
                                    <img
                                        src={SearchIcon}
                                        alt="Иконка личных сообщений"
                                    />
                                </li>
                                <li className="main-list_item ">
                                    <img
                                        src={ChatIcon}
                                        alt="Иконка личных сообщений"
                                    />
                                    <span>1</span>
                                </li>
                                <li className="main-list_item">
                                    <img
                                        src={BellIcon}
                                        alt="Иконка оповещений"
                                    />
                                    <span>1</span>
                                </li>
                                <li className="main-list_item">
                                    <img
                                        src={BookmarkIcon}
                                        alt="Иконка избранные товары"
                                    />
                                    <span>1</span>
                                </li>
                                <li className="main-list_item">
                                    <img
                                        src={ProfileIcon}
                                        alt="Иконка профиля"
                                    />
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </header>
    );
};
