import React from "react";
import { AttentionSwiper } from "../components/UI/AttentionSwiper/AttentionSwiper";
import Img from "../assets/img/20c74a6fd59a8dd8bb8277f84f0aea2b.jpg";
import BookmarkIcon from "../assets/icons/bookmark-icon.svg";
import ArrowIcon2 from "../assets/icons/arrow2.svg";
import Footer from "../components/Footer/Footer";

export const HomePage = () => {
    return (
        <div className="home space-y-5">
            <div className="home-box container mx-auto space-y-5 mt-5">
                <section className="home-attention space-y-5">
                    <div className="attention-swiper bg-white w-full rounded-lg shadow-sm">
                        <div className="attention-heading border-solid border-[2px] border-r-0 border-t-0 border-l-0 border-gray-200">
                            <h1 className="text-xl font-bold p-2 text-center">
                                Обратите внимание
                            </h1>
                        </div>
                        <AttentionSwiper />
                    </div>
                </section>
                <section className="home-advert__list space-y-5 bg-white p-5">
                    <div className="border-solid border-[2px] border-r-0 border-t-0 border-l-0 border-gray-200">
                        <h1 className="text-xl font-bold p-2 text-center">
                            Недавно добавленные обьявления
                        </h1>
                    </div>
                    <div className="home-advert__box grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xxl:grid-cols-4 gap-3 justify-items-center p-2">
                        <div className="advert group/advert shadow-md h-[340px] w-80 overflow-hidden hover:scale-105">
                            <div className="advert__box bg-white p-3 rounded-lg">
                                <div className="advert__img w-full relative">
                                    <img className="cover " src={Img} alt="" />
                                    <button className="absolute top-3 p-1 right-4 rounded-full bg-gray-300 opacity-40 group-hover/advert:opacity-100 transition-all hover:bg-primary-color ">
                                        <img
                                            className="w-6"
                                            src={BookmarkIcon}
                                            alt=""
                                        />
                                    </button>
                                </div>
                                <div className="advert__desc max-w-max relative">
                                    <h4 className="font-bold text-xl h-[90px] overflow-hidden">
                                        Lorem ipsum, dolor sit amet consectetur
                                    </h4>
                                    <p className="flex flex-col text-sm">
                                        <span>Сегодня в 13:54</span>
                                        <span>Молдова, Кишинев</span>
                                    </p>
                                    <p className="flex items-center gap-x-2 font-bold underline underline-offset-4">
                                        <span>
                                            59999 <span>rub.</span>
                                        </span>
                                    </p>
                                    <div className="absolute -bottom-6 -right-6   ">
                                        <button className="rounded-full bg-primary-color p-7 hover:bg-second-dark-color transition-colors">
                                            <img
                                                className=" w-6"
                                                src={ArrowIcon2}
                                                alt=""
                                            />
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="advert group/advert shadow-md h-[340px] w-80 overflow-hidden hover:scale-105">
                            <div className="advert__box bg-white p-3 rounded-lg">
                                <div className="advert__img w-full relative">
                                    <img className="cover " src={Img} alt="" />
                                    <button className="absolute top-3 p-1 right-4 rounded-full bg-gray-300 opacity-40 group-hover/advert:opacity-100 transition-all hover:bg-primary-color ">
                                        <img
                                            className="w-6"
                                            src={BookmarkIcon}
                                            alt=""
                                        />
                                    </button>
                                </div>
                                <div className="advert__desc max-w-max ">
                                    <h4 className="font-bold text-xl h-[90px] overflow-hidden">
                                        Lorem ipsum, dolor sit amet consectetur
                                    </h4>
                                    <p className="flex flex-col text-sm">
                                        <span>Сегодня в 13:54</span>
                                        <span>Молдова, Кишинев</span>
                                    </p>
                                    <p className="flex items-center gap-x-2 font-bold ">
                                        <span>59999</span>
                                        <span>rub</span>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="advert group/advert shadow-md h-[340px] w-80 overflow-hidden hover:scale-105">
                            <div className="advert__box bg-white p-3 rounded-lg">
                                <div className="advert__img w-full relative">
                                    <img className="cover " src={Img} alt="" />
                                    <button className="absolute top-3 p-1 right-4 rounded-full bg-gray-300 opacity-40 group-hover/advert:opacity-100 transition-all hover:bg-primary-color ">
                                        <img
                                            className="w-6"
                                            src={BookmarkIcon}
                                            alt=""
                                        />
                                    </button>
                                </div>
                                <div className="advert__desc max-w-max ">
                                    <h4 className="font-bold text-xl h-[90px] overflow-hidden">
                                        Lorem ipsum, dolor sit amet consectetur
                                    </h4>
                                    <p className="flex flex-col text-sm">
                                        <span>Сегодня в 13:54</span>
                                        <span>Молдова, Кишинев</span>
                                    </p>
                                    <p className="flex items-center gap-x-2 font-bold ">
                                        <span>59999</span>
                                        <span>rub</span>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="advert group/advert shadow-md h-[340px] w-80 overflow-hidden hover:scale-105">
                            <div className="advert__box bg-white p-3 rounded-lg">
                                <div className="advert__img w-full relative">
                                    <img className="cover " src={Img} alt="" />
                                    <button className="absolute top-3 p-1 right-4 rounded-full bg-gray-300 opacity-40 group-hover/advert:opacity-100 transition-all hover:bg-primary-color ">
                                        <img
                                            className="w-6"
                                            src={BookmarkIcon}
                                            alt=""
                                        />
                                    </button>
                                </div>
                                <div className="advert__desc max-w-max ">
                                    <h4 className="font-bold text-xl h-[90px] overflow-hidden">
                                        Lorem ipsum, dolor sit amet consectetur
                                    </h4>
                                    <p className="flex flex-col text-sm">
                                        <span>Сегодня в 13:54</span>
                                        <span>Молдова, Кишинев</span>
                                    </p>
                                    <p className="flex items-center gap-x-2 font-bold ">
                                        <span>59999</span>
                                        <span>rub</span>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="advert group/advert shadow-md h-[340px] w-80 overflow-hidden hover:scale-105">
                            <div className="advert__box bg-white p-3 rounded-lg">
                                <div className="advert__img w-full relative">
                                    <img className="cover " src={Img} alt="" />
                                    <button className="absolute top-3 p-1 right-4 rounded-full bg-gray-300 opacity-40 group-hover/advert:opacity-100 transition-all hover:bg-primary-color ">
                                        <img
                                            className="w-6"
                                            src={BookmarkIcon}
                                            alt=""
                                        />
                                    </button>
                                </div>
                                <div className="advert__desc max-w-max ">
                                    <h4 className="font-bold text-xl h-[90px] overflow-hidden">
                                        Lorem ipsum, dolor sit amet consectetur
                                    </h4>
                                    <p className="flex flex-col text-sm">
                                        <span>Сегодня в 13:54</span>
                                        <span>Молдова, Кишинев</span>
                                    </p>
                                    <p className="flex items-center gap-x-2 font-bold ">
                                        <span>59999</span>
                                        <span>rub</span>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="advert group/advert shadow-md h-[340px] w-80 overflow-hidden hover:scale-105">
                            <div className="advert__box bg-white p-3 rounded-lg">
                                <div className="advert__img w-full relative">
                                    <img className="cover " src={Img} alt="" />
                                    <button className="absolute top-3 p-1 right-4 rounded-full bg-gray-300 opacity-40 group-hover/advert:opacity-100 transition-all hover:bg-primary-color ">
                                        <img
                                            className="w-6"
                                            src={BookmarkIcon}
                                            alt=""
                                        />
                                    </button>
                                </div>
                                <div className="advert__desc max-w-max ">
                                    <h4 className="font-bold text-xl h-[90px] overflow-hidden">
                                        Lorem ipsum, dolor sit amet consectetur
                                    </h4>
                                    <p className="flex flex-col text-sm">
                                        <span>Сегодня в 13:54</span>
                                        <span>Молдова, Кишинев</span>
                                    </p>
                                    <p className="flex items-center gap-x-2 font-bold ">
                                        <span>59999</span>
                                        <span>rub</span>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="advert group/advert shadow-md h-[340px] w-80 overflow-hidden hover:scale-105">
                            <div className="advert__box bg-white p-3 rounded-lg">
                                <div className="advert__img w-full relative">
                                    <img className="cover " src={Img} alt="" />
                                    <button className="absolute top-3 p-1 right-4 rounded-full bg-gray-300 opacity-40 group-hover/advert:opacity-100 transition-all hover:bg-primary-color ">
                                        <img
                                            className="w-6"
                                            src={BookmarkIcon}
                                            alt=""
                                        />
                                    </button>
                                </div>
                                <div className="advert__desc max-w-max ">
                                    <h4 className="font-bold text-xl h-[90px] overflow-hidden">
                                        Lorem ipsum, dolor sit amet consectetur
                                    </h4>
                                    <p className="flex flex-col text-sm">
                                        <span>Сегодня в 13:54</span>
                                        <span>Молдова, Кишинев</span>
                                    </p>
                                    <p className="flex items-center gap-x-2 font-bold ">
                                        <span>59999</span>
                                        <span>rub</span>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className="advert group/advert shadow-md h-[340px] w-80 overflow-hidden hover:scale-105">
                            <div className="advert__box bg-white p-3 rounded-lg">
                                <div className="advert__img w-full relative">
                                    <img className="cover " src={Img} alt="" />
                                    <button className="absolute top-3 p-1 right-4 rounded-full bg-gray-300 opacity-40 group-hover/advert:opacity-100 transition-all hover:bg-primary-color ">
                                        <img
                                            className="w-6"
                                            src={BookmarkIcon}
                                            alt=""
                                        />
                                    </button>
                                </div>
                                <div className="advert__desc max-w-max ">
                                    <h4 className="font-bold text-xl h-[90px] overflow-hidden">
                                        Lorem ipsum, dolor sit amet consectetur
                                    </h4>
                                    <p className="flex flex-col text-sm">
                                        <span>Сегодня в 13:54</span>
                                        <span>Молдова, Кишинев</span>
                                    </p>
                                    <p className="flex items-center gap-x-2 font-bold ">
                                        <span>59999</span>
                                        <span>rub</span>
                                    </p>
                                </div>
                            </div>
                        </div>{" "}
                        <div className="advert group/advert shadow-md h-[340px] w-80 overflow-hidden hover:scale-105">
                            <div className="advert__box bg-white p-3 rounded-lg">
                                <div className="advert__img w-full relative">
                                    <img className="cover " src={Img} alt="" />
                                    <button className="absolute top-3 p-1 right-4 rounded-full bg-gray-300 opacity-40 group-hover/advert:opacity-100 transition-all hover:bg-primary-color ">
                                        <img
                                            className="w-6"
                                            src={BookmarkIcon}
                                            alt=""
                                        />
                                    </button>
                                </div>
                                <div className="advert__desc max-w-max ">
                                    <h4 className="font-bold text-xl h-[90px] overflow-hidden">
                                        Lorem ipsum, dolor sit amet consectetur
                                    </h4>
                                    <p className="flex flex-col text-sm">
                                        <span>Сегодня в 13:54</span>
                                        <span>Молдова, Кишинев</span>
                                    </p>
                                    <p className="flex items-center gap-x-2 font-bold ">
                                        <span>59999</span>
                                        <span>rub</span>
                                    </p>
                                    <div></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
            <Footer />
        </div>
    );
};
