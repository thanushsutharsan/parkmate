// loads parking images from wikimedia commons
document.addEventListener("DOMContentLoaded", () => {
    const fallback =
        document.body.dataset.parkingFallback || "";

    const images = document.querySelectorAll(
        "[data-parking-image]"
    );

    const commonsEndpoint =
        "https://commons.wikimedia.org/w/api.php";

    async function searchCommons(searchText) {
        const params = new URLSearchParams({
            action: "query",
            generator: "search",
            gsrsearch: searchText,
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

                if (imageUrl) {
                    return imageUrl;
                }
            }
        } catch (error) {
            return null;
        }

        return null;
    }

    async function searchNearby(
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
            ggsradius: "1000",
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

                if (imageUrl) {
                    return imageUrl;
                }
            }
        } catch (error) {
            return null;
        }

        return null;
    }

    async function loadImage(image) {
        const fullSearch =
            image.dataset.parkingImage || "";

        const latitude =
            image.dataset.latitude || "";

        const longitude =
            image.dataset.longitude || "";

        let commonsImage = null;

        if (fullSearch) {
            commonsImage =
                await searchCommons(fullSearch);
        }

        if (!commonsImage && fullSearch) {
            const locationName =
                fullSearch.split(",")[0];

            commonsImage =
                await searchCommons(locationName);
        }

        if (!commonsImage) {
            commonsImage =
                await searchNearby(
                    latitude,
                    longitude
                );
        }

        if (commonsImage) {
            image.src = commonsImage;
            return;
        }

        if (fallback) {
            image.src = fallback;
        }
    }

    images.forEach((image) => {
        loadImage(image);
    });
});