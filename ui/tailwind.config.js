/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{js,jsx,ts,tsx}"],
    theme: {
        extend: {
            colors: {
                "primary-color": "#ff6b6b",
                "second-color": "hsla(266, 72%, 45%, 0.88)",
                "hover-color": "#794afa",
                "second-dark-color": "hsla(266, 72%, 16%, 0.88)",
                "red-color": "hsla(360, 100%, 35%, 0.65)",
            },
            screens: {
                mobile: "360px",
                xs: "480px",
                sm: "640px",
                md: "768px",
                lg: "1024px",
                xl: "1280px",
            },
        },
    },
    plugins: [],
};
