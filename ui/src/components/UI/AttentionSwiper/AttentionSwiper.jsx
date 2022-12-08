import React from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import "swiper/css/navigation";
import { Navigation, A11y, Autoplay } from "swiper";
import { AdvertCardAttention } from "../AdvertCardAttention/AdvertCardAttention";
export const AttentionSwiper = () => {
    return (
        <Swiper
            spaceBetween={10}
            navigation={true}
            autoplay={{
                delay: 2500,
                disableOnInteraction: false,
                pauseOnMouseEnter: true,
            }}
            breakpoints={{
                280: {
                    slidesPerView: 1,
                },
                320: {
                    slidesPerView: 1,
                },
                768: {
                    slidesPerView: 2,
                },
                1024: {
                    slidesPerView: 3,
                },
                1280: {
                    slidesPerView: 4,
                },
                1550: {
                    slidesPerView: 5,
                },
            }}
            modules={[Navigation, A11y, Autoplay]}
            className="attention-swiper"
        >
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
            <SwiperSlide>
                <AdvertCardAttention />
            </SwiperSlide>
        </Swiper>
    );
};
