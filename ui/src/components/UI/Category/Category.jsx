import React from "react";
import ArrowIcon from "../../../assets/icons/arrow.svg";

export const Category = ({ dropdownVisible, showDropdown }) => {
    return (
        <div className=" category-dropdown group-hover/category-icon:block hidden">
            <div className="dropdown-container ">
                <ul>
                    <li>
                        <div
                            className="category-main group"
                            onClick={showDropdown}
                        >
                            <span>Транспорт</span>
                            <img
                                className="dropdown-arrow group-hover:block hidden"
                                src={ArrowIcon}
                                alt="стрелочка вложенной раскрывающая вложенные категории"
                            />
                        </div>
                        <ul
                            className={`dropdown ${
                                !dropdownVisible ? "" : "dropdown-show"
                            } `}
                        >
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                        </ul>
                    </li>

                    <li>
                        <div
                            className="category-main group"
                            onClick={showDropdown}
                        >
                            <span>Транспорт</span>
                            <img
                                className="dropdown-arrow group-hover:block hidden"
                                src={ArrowIcon}
                                alt="стрелочка вложенной раскрывающая вложенные категории"
                            />
                        </div>
                        <ul
                            className={`dropdown ${
                                !dropdownVisible ? "max-h-0" : "dropdown-show"
                            } `}
                        >
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                            <li>Автомобили</li>
                        </ul>
                    </li>
                </ul>
                <div className="btn">
                    <button className="category-btn group/btn">
                        Все категории
                        <span className="group-hover/btn:translate-x-2">
                            <img
                                src={ArrowIcon}
                                alt="иконка для перехода ко всем категориям"
                            />
                        </span>
                    </button>
                </div>
            </div>
        </div>
    );
};
