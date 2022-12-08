import React from "react";
import { AttentionSwiper } from "../components/UI/AttentionSwiper/AttentionSwiper";

export const HomePage = () => {
    return (
        <div className="home">
            <div className="home-box container mx-auto space-y-5 mt-5">
                <section className="home-attention space-y-5 ">
                    <div className="attention-swiper bg-white w-full rounded-lg shadow-sm">
                        <div className="attention-heading border-solid border-[2px] border-r-0 border-t-0 border-l-0 border-gray-200">
                            <h1 className="text-xl font-bold p-2 text-center">
                                Обратите внимание
                            </h1>
                        </div>
                        <AttentionSwiper />
                    </div>
                </section>
                <section className="home-products">
                    <div className="home-products__box"></div>
                </section>
            </div>
        </div>
    );
};
