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
            gsrsearch: `${searchText} car park`,
            gsrnamespace: "6",
            gsrlimit: "10",
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

    async function findNearbyImage(
        latitude,
        longitude
    ) {
        if (!latitude || !longitude) {
            return null;
        }

        const params = new URLSearchParams({
            action: "query",
            generator: "geosearch",
            ggsprimary: "all",
            ggsnamespace: "6",
            ggsradius: "500",
            ggslimit: "10",
            ggscoord: `${latitude}|${longitude}`,
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

        const latitude =
            image.dataset.latitude || "";

        const longitude =
            image.dataset.longitude || "";

        let triedCommons = false;

        async function useCommons() {
            if (triedCommons) {
                useFallback();
                return;
            }

            triedCommons = true;

            let commonsImage = null;

            if (searchText) {
                commonsImage =
                    await findCommonsImage(
                        searchText
                    );
            }

            if (!commonsImage) {
                commonsImage =
                    await findNearbyImage(
                        latitude,
                        longitude
                    );
            }

            if (commonsImage) {
                image.src = commonsImage;
                return;
            }

            useFallback();
        }

        function useFallback() {
            if (
                fallback &&
                !image.src.endsWith(
                    "parking-fallback.svg"
                )
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

        const usingFallback =
            fallback &&
            image.src.includes(
                "parking-fallback.svg"
            );

        if (
            !image.getAttribute("src") ||
            image.src === window.location.href ||
            usingFallback
        ) {
            await useCommons();
        }
    }

    images.forEach((image) => {
        loadImage(image);
    });
});