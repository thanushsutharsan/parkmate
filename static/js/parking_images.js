// Loads parking images and uses a fallback when needed.
document.addEventListener("DOMContentLoaded", () => {
    const fallback =
        document.body.dataset.parkingFallback || "";

    const images = document.querySelectorAll(
        "[data-parking-image]"
    );

    const commonsEndpoint =
        "https://commons.wikimedia.org/w/api.php";

    async function findCommonsImage(searchText) {
        const params = new URLSearchParams({
            action: "query",
            generator: "search",
            gsrsearch: `${searchText} parking`,
            gsrnamespace: "6",
            gsrlimit: "5",
            prop: "imageinfo",
            iiprop: "url",
            iiurlwidth: "900",
            format: "json",
            origin: "*",
        });

        try {
            const response = await fetch(
                `${commonsEndpoint}?${params}`
            );

            if (!response.ok) {
                return null;
            }

            const data = await response.json();

            if (!data.query || !data.query.pages) {
                return null;
            }

            const pages = Object.values(
                data.query.pages
            );

            for (const page of pages) {
                const info =
                    page.imageinfo &&
                    page.imageinfo[0];

                if (!info) {
                    continue;
                }

                const imageUrl =
                    info.thumburl ||
                    info.url;

                if (!imageUrl) {
                    continue;
                }

                return imageUrl;
            }
        } catch (error) {
            return null;
        }

        return null;
    }

    async function loadImage(image) {
        const searchText =
            image.dataset.parkingImage || "";

        let triedCommons = false;

        async function useCommons() {
            if (
                triedCommons ||
                !searchText
            ) {
                useFallback();
                return;
            }

            triedCommons = true;

            const commonsImage =
                await findCommonsImage(
                    searchText
                );

            if (commonsImage) {
                image.src = commonsImage;
                return;
            }

            useFallback();
        }

        function useFallback() {
            if (
                fallback &&
                image.src !== fallback
            ) {
                image.src = fallback;
            }
        }

        image.addEventListener(
            "error",
            async () => {
                await useCommons();
            }
        );

        if (
            !image.getAttribute("src") ||
            image.src === window.location.href
        ) {
            await useCommons();
        }
    }

    images.forEach((image) => {
        loadImage(image);
    });
});